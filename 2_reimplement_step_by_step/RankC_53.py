import json
import argparse
import torch
import numpy as np

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    return np.exp(x) / np.sum(np.exp(x), axis=0)

parser = argparse.ArgumentParser()
parser.add_argument(
    '-pair',
    dest='pair',
    default='en,zh',
    help='language pair',
    type=str,
)

parser.add_argument(
    '-mname',
    dest='mname',
    default='bigscience/bloom-3b',
    help='model name',
    type=str,
)

parser.add_argument(
    '-weight',
    dest='weight',
    default='softmax',
    help='weight metric',
    type=str,
)

args = parser.parse_args()
mname = args.mname
pair = args.pair.split(',')
weight_metric = args.weight # softmax norm1 norm2

lang1 = pair[0]
lang2 = pair[1]


fname1 = './record53/' + mname.replace('/','-') + '_Rankings_' + lang1 + '.txt'
fname2 = './record53/' + mname.replace('/','-') + '_Rankings_' + lang2 + '.txt'

fcand1 = './record53/' + mname.replace('/', '-') + '_Scores_' + lang1 + '.txt'
fcand2 = './record53/' + mname.replace('/', '-') + '_Scores_' + lang2 + '.txt'


with open(fname1, 'r') as f1:
    lang1_rankings = json.load(f1)
with open(fname2, 'r') as f2:
    lang2_rankings = json.load(f2)
with open(fcand1, 'r') as f3:
    cand1 = json.load(f3)
    cand1 = eval(cand1)
with open(fcand2, 'r') as f4:
    cand2 = json.load(f4)
    cand2 = eval(cand2)

cand_list1 = [[j for j in list(i.keys())] for i in cand1]
cand_list2 = [[j for j in list(i.keys())] for i in cand2]

num_consistent = 0

for i in range(len(lang1_rankings)):
    ranking1 = lang1_rankings[i]
    ranking2 = lang2_rankings[i]

    candidate1 = cand_list1[i]
    candidate2 = cand_list2[i]
    
    order = [len(ranking1)-i for i in range(len(ranking1))]
    order = np.array(order)
    
    if weight_metric == 'softmax':
        weight = softmax(order)
    elif weight_metric == 'norm1':
        weight = order/np.sum(order)
    else:
        weight = np.power(order, 2)/np.sum(np.power(order, 2))
    
    for j in range(len(ranking1)):
        set1 = {candidate1.index(i) for i in ranking1[:j+1]}
        set2 = {candidate2.index(i) for i in ranking2[:j+1]}
        
        cover = set1.intersection(set2)
        num_consistent += weight[j] * (len(cover)/len(set1))
    
print(num_consistent/len(lang1_rankings))
