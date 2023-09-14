#!/bin/bash

for MODEL in bigscience/bloom-3b google/mt5-large xlm-roberta-large # The models you want to test on
do
for LANG in en fr nl es ru ja zh ko vi el hu he tr ca ar uk fa # The queried languages
do
	python main.py -lang $LANG -mname $MODEL -mini yes
done
done

