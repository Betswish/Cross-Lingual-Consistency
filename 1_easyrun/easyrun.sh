#!/bin/bash

# The models you want to test on
model=bigscience/bloom-3b # bigscience/bloom-3b google/mt5-large xlm-roberta-large

# Language pair
lang1=en # en fr nl es ru ja zh ko vi el hu he tr ca ar uk fa
lang2=fr # en fr nl es ru ja zh ko vi el hu he tr ca ar uk fa

# BMLAMA17
mini=yes # no, using BMLAMA53


# Run Probing

if [ ! -f "$file" ]; then
  touch "$file"
fi

python main.py -lang $lang1 -mname $model -mini $mini
python main.py -lang $lang2 -mname $model -mini $mini

# Calculating CLC with RankC
weight=softmax # softmax norm1 norm2

echo $model $lang1 $lang2
python RankC.py -pair $lang1,$lang2 -mname $mname -weight $weight -mini $mini