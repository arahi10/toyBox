from base import *
from puyo import StaticPuyo
ans = []
DODAI = [
"  XXXX",
"GRXXXX",
"GGRXXX",
"RRBXXX"]

puyos = [[StaticPuyo(i,j,t.get(DODAI[i][j],0))for j in range(MAXRETU)] for i in range(MAXDAN)]
ijs = [(i,j)for i in range(MAXDAN)for j in range(MAXRETU) if DODAI[i][j]=='X']
ij2ind = {ij:ind for ind,ij in enumerate(ijs)}
ANS = 0
for i in range(3):
    for j in range(1,4):
        if DODAI[i][j]!="X":
            for ai,aj in make_parent(i,j):
                puyos[i][j].touchWithoutVanish(puyos[ai][aj])
print('\n'.join('  #  '.join(map(lambda x:x.detail(),l))for l in puyos))
def rec(it=0):
    if it == len(ijs):
        print("[",*puyos,"]",sep='\n')
        print('\n'.join('  #  '.join(map(lambda x:x.detail(),l))for l in puyos))
        print()

        return
    i,j = ijs[it]
    if puyos[i][j].color != 0:
        if not puyos[i][j].touchWithoutVanish(puyos[i-1][j]):
            return
        rec(it+1)
        return 
    for col in [RED, GREEN, BLUE, YELLOW]:
        puyos[i][j] = StaticPuyo(i,j,col)
        if all(puyos[i][j].touchWithoutVanish(puyos[pi][pj])for pi , pj in make_parent(i,j)):
            rec(it+1)
        puyos[i][j].disconnect()
rec()
with open('result.txt','w') as f:
    f.write(str(ans))