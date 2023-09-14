weight=softmax # softmax norm1 norm2

#for mname in bigscience/bloom-3b google/mt5-large xlm-roberta-large
for mname in bigscience/bloom-3b
do
	for lang1 in ca az en ar uk fa tr it el ru hr hi sv sq fr ga eu de nl et he es bn ms sr hy ur hu la sl cs af gl fi ro ko cy th be id pt vi ka ja da bg zh pl lv sk lt ta ceb
	do
		for lang2 in ca az en ar uk fa tr it el ru hr hi sv sq fr ga eu de nl et he es bn ms sr hy ur hu la sl cs af gl fi ro ko cy th be id pt vi ka ja da bg zh pl lv sk lt ta ceb
		do
			echo $mname $lang1 $lang2
			python RankC_53.py -pair $lang1,$lang2 -mname $mname -weight $weight
done
done
done

exit 0
