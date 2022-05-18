from base import *
from puyo import StaticPuyo
ans = [] #実行可能解記録用
DODAI = [
"  XXXX",
"GRXXXX",
"GGRXXX",
"RRBXXX"]
# 解構築のためのスタック変数
puyos = [[StaticPuyo(i,j,t.get(DODAI[i][j],0))for j in range(MAXRETU)] for i in range(MAXDAN)]
# X(全探索する領域)とそれに連結しうる土台部分のインデックスを列挙
ijs = [(i,j)for i in range(MAXDAN)for j in range(2,MAXRETU) ]
# 変換用
ij2ind = {ij:ind for ind,ij in enumerate(ijs)}
# デバッグ用変数、多分使ってない
ANS = 0
#GTR部分の連結処理をする
for i in range(1,MAXDAN):
    for j in range(MAXRETU):
        if DODAI[i][j]!="X":
            for ai,aj in make_children(i,j):
                puyos[i][j].touchWithoutVanish(puyos[ai][aj])
#print debug
print('\n'.join('  #  '.join(map(lambda x:x.detail(),l))for l in puyos))
# 再帰で解の構築を行う。解の構築用の変数はpuyos
def rec(it=0):
    global puyos
    if it == len(ijs):
        print("[",*puyos,"]",sep='\n')
        print('\n'.join('  #  '.join(map(lambda x:x.detail(),l))for l in puyos))
        print()

        return
    i,j = ijs[it]
    if puyos[i][j].color != 0:
        #GTRの土台で確定してる部分(もっと言えばGTRの鼻部分のR(Bの方はこの時点では右のXに色は振り分けてないので考慮しない))
        if not puyos[i][j].touchWithoutVanish(puyos[i-1][j]):
            # 現在の解ではGTRの鼻部分が消える
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
