from collections import defaultdict
from operator import itemgetter as it
from base import *
res = defaultdict(int)
print('start')
if ZABUTON:
    DUMPFILE_ANOTHER = 'result_zabuton.txt'
    DUMPFILE_SAME = 'result_zabuton2.txt'
    CONCATE_FILE = 'all_zabuton.txt'
else:
    DUMPFILE_ANOTHER = 'result.txt'
    DUMPFILE_SAME = 'result2.txt'
    CONCATE_FILE = 'all.txt'

with open(DUMPFILE_ANOTHER, 'r') as file:
    while (line1 := file.readline()) and (line2 := file.readline()):
        _, cnt = line1.split(" : ")
        if ZABUTON:
            res[line2] += int(cnt)
        else:
            res[line2] += int(cnt) << 1
with open(DUMPFILE_SAME, 'r') as file:
    while (line1 := file.readline()) and (line2 := file.readline()):
        _, cnt = line1.split(" : ")
        res[line2] += int(cnt)

ans = list(res.items())

ans.sort(key=it(1), reverse=True)
with open(CONCATE_FILE, 'w') as file:
    for i, (k, v) in enumerate(ans):
        file.write(f"{i} : {v}"+"\n"+k.replace(',', '\n')+"\n")
