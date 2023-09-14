weight=softmax # softmax norm1 norm2

#for mname in bigscience/bloom-3b google/mt5-large xlm-roberta-large
for mname in bigscience/bloom-3b
do
	for lang1 in en fr nl es ru ja zh ko vi el hu he tr ca ar uk fa
	do
		for lang2 in en fr nl es ru ja zh ko vi el hu he tr ca ar uk fa
		do
			echo $mname $lang1 $lang2
			python RankC_17.py -pair $lang1,$lang2 -mname $mname -weight $weight
done
done
done

exit 0
