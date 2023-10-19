# Cross-Lingual Consistency (CLC) of Factual Knowledge in Multilingual Language Models

## Environment: 
Python version: 3.11

Packages: `pip install -r requirements.txt`

## 1 Easyrun
For a quick start, run the following two lines to get the CLC of two languages in a PLM:
```bash
cd 1_easyrun
bash easyrun.sh
```

You can modify the variables in easyrun.sh
- `mname`: Model name on Huggingface.
- `lang1` & `lang2`: Abbreviation of languages in ISO 639-1 format. See tables below for details.
- `mini`: `yes` for using BMLAMA-17 (`yes`) and `no` for using BMLAMA-53.
- `weight`: Weight metric for RankC, choose among `softmax` `norm1` `norm2`.
 
|  Language (BMLAMA-17)  |  ISO 639-1     | Language (BMLAMA-17)  |  ISO 639-1 |
| ---------------------- | ----------------- | ---------------------- | ----------------- | 
|    | en |    | fr  |
|    | nl |    | es  |
|    | ru |    | ja  |
|    | zh |    | ko  |
|    | vi |    | el  |
|    | hu |    | he  |
|    | tr |    | ca  |
|    | ar |    | uk  |
|    | fa |  

|  Language (BMLAMA-53)  |  ISO 639-1  |  Language (BMLAMA-53)  |  ISO 639-1  |  Language (BMLAMA-53)  |  ISO 639-1  |
| ---------------------- | ----------------- | ---------------------- | ----------------- | ---------------------- | ----------------- | 
|    | ca |    |  az  |    |  en  |
|    | ar |    |  uk  |    |  fa  |
|    | tr |    |  it  |    |  el  |
|    | ru |    |  hr  |    |  hi  |
|    | sv |    |  sq  |    |  fr  |
|    | ga |    |  eu  |    |  de  |
|    | nl |    |  et  |    |  he  |
|    | es |    |  bn  |    |  ms  |
|    | sr |    |  hy  |    |  ur  |
|    | hu |    |  la  |    |  sl  |
|    | cs |    |  af  |    |  gl  |
|    | fi |    |  ro  |    |  ko  |
|    | cy |    |  th  |    |  be  |
|    | id |    |  pt  |    |  vi  |
|    | ka |    |  ja  |    |  da  |
|    | bg |    |  zh  |    |  pl  |
|    | lv |    |  sk  |    |  lt  |
|    | ta |    |  ceb |



## 2 Reimplement Step by Step  (Working in process)

