#!/bin/bash

# The model you want to test on
model=bigscience/bloom-3b # bigscience/bloom-3b google/mt5-large xlm-roberta-large
# Language pair
lang1=en # en fr nl es ru ja zh ko vi el hu he tr ca ar uk fa
lang2=fr # en fr nl es ru ja zh ko vi el hu he tr ca ar uk fa
# Dataset
mini=yes # 'yes' for using BMLAMA17; 'no' for using BMLAMA53
# Weight Metric
weight=softmax # softmax norm1 norm2

# Run Probing (No need for changing)
for LANG in $lang1 $lang2
do
  python main.py -lang $LANG -mname $model -mini $mini
done

# Calculating CLC with RankC (No need for changing)
echo $model $lang1 $lang2
python RankC.py -pair $lang1,$lang2 -mname $mname -weight $weight -mini $mini
