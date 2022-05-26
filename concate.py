from collections import defaultdict
from operator import itemgetter as it
res=defaultdict(int)
print('yey')
DUMPFILE_ANOTHER = 'result_zabuton.txt'
DUMPFILE_SAME = 'result_zabuton2.txt'
CONCATE_FILE = 'all_zabuton.txt'
with open(DUMPFILE_ANOTHER,'r') as file :
    while (line1 := file.readline()) and (line2 := file.readline()):
        _,cnt = line1.split(" : ")
        res[line2]+=int(cnt)<<1
with open(DUMPFILE_SAME,'r') as file :
    while (line1 := file.readline()) and (line2 := file.readline()):
        _,cnt = line1.split(" : ")
        res[line2]+=int(cnt)
ans = list(res.items())

ans.sort(key = it(1),reverse= True)
print(ans[:10])
with open(CONCATE_FILE,'w') as file:
    for i,(k,v)in enumerate(ans):
        file.write(f"{i} : {v}"+"\n"+k.replace(',','\n')+"\n")