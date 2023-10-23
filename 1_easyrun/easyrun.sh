#!/bin/bash

# The model you want to test on
mname=bigscience/bloom-3b # bigscience/bloom-3b google/mt5-large xlm-roberta-large
# Language pair
# For BMLAMA-17:
# en fr nl es ru ja zh ko vi el hu he tr ca ar uk fa
# For BMLAMA-53:
# ca az en ar uk fa tr it el ru hr hi sv
# sq fr ga eu de nl et he es bn ms sr hy
# ur hu la sl cs af gl fi ro ko cy th be
# id pt vi ka ja da bg zh pl lv sk lt ta ceb
lang1=en
lang2=fr
# Dataset
mini=yes # 'yes' for using BMLAMA17; 'no' for using BMLAMA53
# Weight Metric
weight=softmax # softmax norm1 norm2

# Run Probing (No need for changing)
for LANG in $lang1 $lang2
do
  python main.py -lang $LANG -mname $mname -mini $mini
done

# Calculating CLC with RankC (No need for changing)
echo $mname $lang1 $lang2
python RankC.py -pair $lang1,$lang2 -mname $mname -weight $weight -mini $mini
