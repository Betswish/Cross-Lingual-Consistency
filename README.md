# Cross-Lingual Consistency (CLC) of Factual Knowledge in Multilingual Language Models

## Environment: 
Python: 3.11

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

- Supported languages of BMLAMA-17:
  
| Language  | ISO 639-1 | Language  | ISO 639-1 | Language   | ISO 639-1 |
| --------- | --------- | --------- | --------- | ---------- | --------- | 
| English   |     en    | French    |     fr    | Dutch      |     nl    |
| Spanish   |     es    | Russian   |     ru    | Japanese   |     ja    |
| Chinese   |     zh    | Korean    |     ko    | Vietnamese |     vi    |
| Greek     |     el    | Hungarian |     hu    | Hebrew     |     he    |
| Turkish   |     tr    | Catalan   |     ca    | Arabic     |     ar    |
| Ukrainian |     uk    | Persian   |     fa    |            |           |

- Supported languages of BMLAMA-53:
  
| Language | ISO 639-1 | Language | ISO 639-1 | Language | ISO 639-1 |
| ------- | -------- | ----------- | ---------- | ------ | --------- | 
|Catalan | ca |Azerbaijani | az | English | en |
|Arabic	 | ar |Ukrainian | uk |Persian | fa |
|Turkish | tr |Italian | it |Greek | el |
|Russian | ru |Croatian | hr |Hindi | hi |
|Swedish | sv |Albanian | sq |French | fr |
|Irish | ga | | eu | | de |
|Dutch | nl | | et | | he |
|Spanish | es | | bn | | ms |
|Serbian | sr | | hy | | ur |
|Hungarian | hu | | la | | sl |
|Czech | cs | | af | | gl |
|Finnish | fi | | ro | | ko |
|Welsh | cy | | th | | be |
|Indonesian | id | | pt | | vi |
|Georgian | ka | | ja | | da |
|Bulgarian | bg | | zh | | pl |
|Latvian | lv | | sk | | lt |
|amil | ta | | ceb | | |



## 2 Reimplement Step by Step  (Working in process)

