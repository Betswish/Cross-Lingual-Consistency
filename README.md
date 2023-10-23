# Cross-Lingual Consistency (CLC) of Factual Knowledge in Multilingual Language Models

## Environment: 
Python: 3.11

Packages: `pip install -r requirements.txt`

## Quick Start
For a quick start, you only need to run the following **two** lines to get the CLC of two languages in a PLM:
```bash
cd 1_easyrun
bash easyrun.sh
```

You can modify the variables in easyrun.sh
- `mname`: The model currently supports LLaMA, BLOOM, BLOOMZ, mT5, RoBERTa. Use the full model name on Huggingface! Like `bigscience/bloom-3b`.
- `lang1` & `lang2`: Abbreviation of languages in ISO 639-1 format. See the tables below for details.
- `mini`: `yes` for using BMLAMA-17 and `no` for using BMLAMA-53.
- `weight`: Weight metric for RankC, select among `softmax`, `norm1`, and `norm2`.

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
  
| Language   | ISO 639-1 | Language    | ISO 639-1 | Language   | ISO 639-1 |
| ---------- | --------- | ----------- | --------- | ---------- | --------- | 
| Catalan    |     ca    | Azerbaijani |     az    | English    |     en    |
| Arabic	   |     ar    | Ukrainian   |     uk    | Persian    |     fa    |
| Turkish    |     tr    | Italian     |     it    | Greek      |     el    |
| Russian    |     ru    | Croatian    |     hr    | Hindi      |     hi    |
| Swedish    |     sv    | Albanian    |     sq    | French     |     fr    |
| Irish      |     ga    | Basque      |     eu    | German     |     de    |
| Dutch      |     nl    | Estonian    |     et    | Hebrew     |     he    |
| Spanish    |     es    | Bengali     |     bn    | Malay      |     ms    |
| Serbian    |     sr    | Armenian    |     hy    | Urdu       |     ur    |
| Hungarian  |     hu    | Latin       |     la    | Slovenian  |     sl    |
| Czech      |     cs    | Afrikaans   |     af    | Galician   |     gl    |
| Finnish    |     fi    | Romanian    |     ro    | Korean     |     ko    |
| Welsh      |     cy    | Thai        |     th    | Belarusian |     be    |
| Indonesian |     id    | Portuguese  |     pt    | Vietnamese |     vi    |
| Georgian   |     ka    | Japanese    |     ja    | Danish     |     da    |
| Bulgarian  |     bg    | Chinese     |     zh    | Polish     |     pl    |
| Latvian    |     lv    | Slovak      |     sk    | Lithuanian |     lt    |
| amil       |     ta    | Cebuano     |     ceb   |            |           |

