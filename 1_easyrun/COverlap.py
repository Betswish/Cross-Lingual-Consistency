import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    '-pair',
    dest='pair',
    default='en,zh',
    help='language pair',
    type=str,
)

parser.add_argument(
    '-mname',
    dest='mname',
    default='bigscience/bloom-3b',
    help='model name',
    type=str,
)

parser.add_argument(
    '-mini',
    default='yes',
    help='yes: BMLAMA17; no: BMLAMA53',
    type=str,
)

args = parser.parse_args()
mname = args.mname
pair = args.pair.split(',')

lang1 = pair[0]
lang2 = pair[1]

if args.mini == 'yes':
    folder = './record17/'
else:
    folder = './record53/'

fname1 = folder + mname.replace('/','-') + '_CorrectIndex_' + lang1 + '.txt'
fname2 = folder + mname.replace('/','-') + '_CorrectIndex_' + lang2 + '.txt'

with open(fname1, 'r') as f1:
    lang1_correct = json.load(f1)
with open(fname2, 'r') as f2:
    lang2_correct = json.load(f2)

num_consistent = 0
num_tot_correct = 0
for i in range(len(lang1_correct)):
    ans_length = len(lang1_correct[i])
    num_tmp = 0
    for j in range(ans_length):
        if lang1_correct[i][j] == 1 and lang2_correct[i][j] == 1:
            num_tmp += 1
        if lang1_correct[i][j] == 1 or lang2_correct[i][j] == 1:
            num_tot_correct += 1
    num_consistent += num_tmp/ans_length

print(num_consistent/num_tot_correct)
