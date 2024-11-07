import json
import pickle as pkl
import numpy as np
import os
import argparse
import matplotlib.pyplot as plt

from transformers import pipeline, AutoTokenizer, AutoModelForMaskedLM, AutoModelForCausalLM, XGLMTokenizer, T5ForConditionalGeneration, MT5ForConditionalGeneration, LlamaTokenizer
from sklearn.metrics import f1_score, accuracy_score
from tqdm import tqdm
import torch

def predict_mask(answer_cand, prompt, mname):
    answer_pred_probs = dict()
    
    for answer in answer_cand:
        answer_cand_probs = []
    
        if "t5" not in mname and "xglm" not in mname and "opt" not in mname and "bloom" not in mname and "llama" not in mname and "gpt" not in mname:
            answer_tokens = tokenizer(answer)["input_ids"][1:-1]
    
            if "xlm-roberta" in mname and answer_tokens[0] == 6 and lang == "zh":
                answer_tokens = answer_tokens[1:]
    
            new_mask = ["<mask>"] * len(answer_tokens)
    
            if lang == "zh":
                new_mask = "".join(new_mask)
            else:
                new_mask = " ".join(new_mask)
    
            prompt_new = prompt.replace('<mask>', new_mask)
            prompt_new = prompt_new.replace('<mask>', tokenizer.mask_token)
    
            for j, w_idx in enumerate(answer_tokens):
                model_inputs = tokenizer(prompt_new, return_tensors='pt').to(device)
                model_outputs = model(**model_inputs)
                input_ids = model_inputs["input_ids"][0]
                outputs = model_outputs["logits"]
                masked_index = torch.nonzero(input_ids == tokenizer.mask_token_id, as_tuple=False)
                    
                logits = outputs[0, masked_index[0].item(), :]
                probs = logits.softmax(dim=-1).detach().cpu().numpy()
                answer_cand_probs.append(-np.log(probs[w_idx]))
    
                pos = prompt_new.find(tokenizer.mask_token)
                prompt_new = prompt_new[:pos] + tokenizer.convert_ids_to_tokens(w_idx) + prompt_new[pos+len(tokenizer.mask_token):]
    
            answer_pred_probs[answer] = np.mean(answer_cand_probs)
    
        elif "xglm" in mname or "opt" in mname or "bloom" in mname or "llama" in mname or "gpt" in mname:
            prompt_new = prompt.replace("<mask>", answer)
            
            # Fix the issue that Bloom Tokenizer will not automatically add the BOS token
            if "bloom" in mname: prompt_new = "<s>" + prompt_new
            
            model_input = tokenizer(prompt_new, return_tensors='pt').to(device)
            output = model(**model_input)

            logits = output['logits'][0, :-1] 
            token_ids = model_input['input_ids'][0, 1:]
            
            # if lang == 'zh':
            #     logits = output['logits'][0, :-1] 
            #     token_ids = model_input['input_ids'][0, 1:]
            # else:
            #     logits = output['logits'][0, :-2] 
            #     token_ids = model_input['input_ids'][0, 1:-1]
    
            answer_pred_probs[answer] = float(torch.nn.CrossEntropyLoss(reduction='mean')(logits, token_ids))
        else:
            input_ids = tokenizer(prompt.replace('<mask>', '<extra_id_0>'), return_tensors='pt').input_ids.to(device)
            labels = tokenizer('<extra_id_0> ' + answer + ' <extra_id_1>', return_tensors='pt').input_ids.to(device)
            target_ids = labels[0][1:-2]
    
            outputs = model(input_ids=input_ids, labels=labels).logits
            masked_index = torch.tensor(list(range(outputs.size()[1]))[1:-2])
            
            for idx, t_idx in zip(masked_index, target_ids):
                logits = outputs[0, idx.item(), :]
                probs = logits.softmax(dim=-1).detach().cpu().numpy()
                answer_cand_probs.append(-np.log(probs[t_idx]))
    
            answer_pred_probs[answer] = np.mean(answer_cand_probs)
    
    return answer_pred_probs
    
parser = argparse.ArgumentParser()

parser.add_argument(
    '-lang',
    dest='lang',
    default='en',
    help='language',
    type=str,
)

parser.add_argument(
    '-mname',
    dest='mname',
    default='bert-base-multilingual-cased',
    help='model name',
    type=str,
)

parser.add_argument(
    '-mini',
    default='yes',
    help='yes: BMLAMA17; no: BMLAMA53',
    type=str,
)

args = parser.parse_args()

lang = args.lang

if args.mini == 'yes':
    mini = True
    fname = "BMLAMA17/" + lang + ".tsv"
    folder_name = './record17/'
else:
    mini = False
    fname = "BMLAMA53/" + lang + ".tsv"
    folder_name = './record53/'

mname = args.mname

record_name = folder_name + mname.replace('/', '-') + '_Rankings_' + lang + '.txt'

if not os.path.exists(record_name):
    if "xglm" in mname or "opt" in mname or "bloom" in mname or "llama" in mname or "gpt" in mname:
        model = AutoModelForCausalLM.from_pretrained(mname)
    elif "google/mt5" in mname:
        model = MT5ForConditionalGeneration.from_pretrained(mname)
    elif "t5" in mname:
        model = T5ForConditionalGeneration.from_pretrained(mname)
    else:
        model = AutoModelForMaskedLM.from_pretrained(mname)
    if "xglm" in mname:
        tokenizer = XGLMTokenizer.from_pretrained(mname)
    else:
        tokenizer = AutoTokenizer.from_pretrained(mname)

    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    print("Runing on:" + device)
    print()
    model = model.to(device)

    data = []
    
    with open(fname) as f:
        for line in f:
            d = line.strip().split('\t')
            if d[0] == "Prompt": continue
            if len(d) <= 1:
                continue
            else:
                d[1] = d[1].split(', ')
                d[2] = d[2].split(', ')                
                data.append(d)

    all_gold_ans = []
    answer_pred_orig_probs = dict()
    
    pred_corr = 0
    pred_tot = 0

    # For saving probing results
    correct_index = []
    answer_count = []
    rank = []
    score_full = []

    for i, d in tqdm(enumerate(data)):
    #for i, d in enumerate(data):
        #print(mname, lang, i, '/', len(data))
        
        prompt = d[0]
        gold_ans_list = d[1]
        answer_cand = d[2]
        
        all_gold_ans.append(gold_ans_list)

        answer_pred_probs = predict_mask(answer_cand, prompt, mname)
        sorted_probs = sorted(answer_pred_probs.items(), key=lambda x: x[1], reverse=False)
        
        ranked_keys = [x[0] for x in sorted_probs]
        rank.append(ranked_keys[:])

        score_full.append(answer_pred_probs)

        corr = 0
        tot = len(gold_ans_list)

        correct_gold = [] # New added
        for gold_ans in gold_ans_list:
            if gold_ans in ranked_keys[:tot]:
                corr += 1
                correct_gold.append(1) 
            else: # New added
                correct_gold.append(0) 
        
        correct_index.append(correct_gold)
        answer_count.append(tot)


        pred_corr += corr
        pred_tot += tot


    # Saving probing results to files
    with open(folder_name + mname.replace('/', '-') + '_Rankings_' + lang + '.txt', 'w') as f:
        json.dump(rank, f)

    with open(folder_name + mname.replace('/', '-') + '_Scores_' + lang + '.txt', 'w') as f:
        json.dump(str(score_full), f)

    with open(folder_name + mname.replace('/', '-') + '_CorrectIndex_' + lang + '.txt', 'w') as f:
        json.dump(correct_index, f)
    with open(folder_name + mname.replace('/', '-') + '_AnswerCount_' + lang + '.txt', 'w') as f:
        json.dump(answer_count, f)

    # Print probing accuracy
    print(mname+'_'+lang+': ', [pred_corr/pred_tot])
    print(pred_corr)
    print(pred_tot)
