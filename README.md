Cross-Lingual Consistency of Factual Knowledge in Multilingual Language Models
=======
1_RankC (env: python 3.11)
------------
To re-implement the probing accuracy of BMLAMA-17 and BMLAMA-53,

- Run ``bash test_17.sh`` or ``bash test_53.sh`` to probing BMLAMA-17 and BMLAMA-53.
	
- The correctness and rankings are automatically saved to ``record17/`` folder or ``record53/`` folder

To compute RankC and COverlap scores

- Rankc: run ``bash analyze_rankings_17.sh`` or ``bash analyze_rankings_53.sh`` to get cross-lingual consistency based on RankC metric. 
	- Our results are saved in ``results/``.
- COverlap: run ``bash analyze_onlycorrect.sh`` to get cross-lingual consistency based on COverlap metric. 
	- Our results are saved in ``results/``.


2_correlation (env: python 3.11)
------------
To calculate the Pearson correlation coefficient, we already store all similarity scores between languages in BMLAMA-17 and BMLAMA-53 in these two .py files. Just run!

- ``python correlating_17.py`` and ``python correlating_53.py``

To show the subword overlapping on Flores-200, ``cd 2_1_Flores200`` and run

- ``python check_overlap_17.py`` and ``python check_overlap_53.py``

To show the subword overlapping on BMLAMA, ``cd 2_2_BMLAMA`` and run

- ``python check_overlap_17.py`` and ``python check_overlap_53.py``

To show the typological similarities of languages in BMLAMA-17 and BMLAMA-53, install *lang2vec* by

~~~~
cd 2_3_Typological/lang2vec
python3 setup.py install
~~~~

and download ``wget http://www.cs.cmu.edu/~aanastas/files/distances.zip`` to ``lang2vec/data`` dictionary.

Then go back to ``2_3_Typological`` and run

- ``python check_similarity_17.py`` and ``python check_similarity_53.py``


3_rome (env: python 3.07)
------------
For re-implement counterfactual knowledge in Section 7

To see the probabilities before editing
~~~~
cd notebooks/
python rome_before.py
~~~~
To see the probabilities after editing

~~~~
cd notebooks/
python rome_after.py
~~~~
Queries about 'Steve Jobs worked for' in all languages are:
(If garbled, please see the raw README file.)

- en (-): Steve Jobs worked for
- es (high): Steve Jobs trabajó para
- vi (high): Steve Jobs đã làm việc cho
- hu (low): Steve Jobs a cégnél dolgozott
- el (low): Ο Steve Jobs δούλευε για την
