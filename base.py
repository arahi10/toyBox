
RED = 1
GREEN = 2
BLUE = 3
YELLOW = 4
#MAXRETU = 5
MAXRETU = 6 # 書き換え忘れ
MAXDAN = 4
RENSA = 5 # 全探索領域を使い切ると最大5連鎖になるはず

t = {"R":RED,"B":BLUE,"G":GREEN,"Y":YELLOW}

def retu_dan_to_ij(retu, dan):
    return MAXDAN-dan, retu-1


def make_adjecent(i, j):
    if i != 0:
        yield (i-1, j)
    if j != 0:
        yield (i, j-1)
    if j != MAXRETU-1:
        yield (i, j+1)
    if i != MAXDAN-1:
        yield (i+1, j)
# size (連結数)計算用の親は隣接ぷよのうちインデックスが辞書順で若い人←バグってそう、若くない人では？
# ↑バグってませんでした
def make_childs(i,j):
    if i!=0:
        yield (i-1,j)
    if j!=0:
        yield (i,j-1)
