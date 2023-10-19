# Cross-Lingual Consistency (CLC) of Factual Knowledge in Multilingual Language Models

## Environment: 
Python: 3.11

Packages: `pip install -r requirements.txt`

## 1 Easyrun
For a quick startup, run the following two lines to get the CLC of two languages in a PLM:
```bash
cd 1_easyrun
bash easyrun.sh
```

You can modify the variables in easyrun.sh
- `mname`: model name on Huggingface
- `lang1` & `lang2`: abbreviation of languages in ISO 639-1 format
- `mini`: whether use BMLAMA-17 or BMLAMA-53
- `weight`: weight metric for RankC, choose among 'softmax' 'norm1' 'norm2'


## 2 Reimplement Step by Step  (Working in process)

