#!/bin/bash

for MODEL in bigscience/bloom-3b google/mt5-large xlm-roberta-large
do
for LANG in ca az en ar uk fa tr it el ru hr hi sv sq fr ga eu de nl et he es bn ms sr hy ur hu la sl cs af gl fi ro ko cy th be id pt vi ka ja da bg zh pl lv sk lt ta ceb
do
	python main.py -lang $LANG -mname $MODEL -mini no
done
done

