from base import *
from table import Table
from time import time

OUTPUTFILE = 'hoge.txt'

DODAI = [
    "  XXXX",
    "GRXXXX",
    "GGRXXX",
    "RRBXXX"]
# DODAI = [
#     "  XXXX",
#     "GRXXXX",
#     "GGRXXX",
#     "RRGXXX"]
# DODAI = [
#     "YYYXXX",
#     "GRXXXX",
#     "GGRXXX",
#     "RRBXXX"]
# DODAI = [
#     "YYYXXX",
#     "GRXXXX",
#     "GGRXXX",
#     "RRGXXX"]

color = [
    [-1 if s == "X" else NULL if s == ' ' else t[s]for s in l]
    for l in DODAI]

start = time()


def flatten(i, j):
    return i*MAXRETU+j


def spread(o):
    return o//MAXRETU, o % MAXRETU


def parent(i, tbl):
    return i if tbl[i] < 0 else parent(tbl[i], tbl)


def same(i, j, tbl):
    return parent(i, tbl) == parent(j, tbl)


def size(i, tbl):
    return -tbl[parent(i, tbl)]


def unite(i, j, tbl: list):
    if same(i, j, tbl):
        return True
    if size(i, tbl)+size(j, tbl) >= 4:
        return False
    else:
        i, j = parent(i, tbl), parent(j, tbl)
        tbl[j] += tbl[i]
        tbl[i] = j
        return True


def memo():
    global pool, start
    # with open("result.txt",'w') as file:
    with open(OUTPUTFILE, 'w') as file:
        for i, (k, v) in enumerate(pool.items()):
            file.write(f"{i} : {v}\n{k}\n")
    print(time()-start)


pool = {}
#ANS =0


def rec(ind, i, j, *tbl):
    global color, pool  # , ANS
    if ind == MAXDAN*MAXRETU:
        tmp = Table(color)
        ret = tmp.chain()
        if ret:
            key = show(ret)
            if key in pool:
                pool[key] += 1
            else:
                pool[key] = 1
            # ANS += 1
            # print(*color,'',sep='\n')
            # if ANS == 6:
            #     memo()
            #     exit()
        return
    if color[i][j] != -1:
        col = color[i][j]
        this = list(tbl)
        for ci, cj in make_children(i, j):
            if col == color[ci][cj]:
                if not unite(ind, flatten(ci, cj), this):
                    break
        else:
            rec(ind+1, *spread(ind+1), *this)
    else:
        old = tbl
        for col in (RED, GREEN, BLUE, YELLOW):
            color[i][j] = col
            this = list(tbl)
            for ci, cj in make_children(i, j):
                if col == color[ci][cj]:
                    if not unite(ind, flatten(ci, cj), this):
                        break
            else:
                rec(ind+1, *spread(ind+1), *this)
            tbl = old
            color[i][j] = -1


table = [-1]*(MAXDAN*MAXRETU)

Gs = [MAXRETU, 2*MAXRETU, 2*MAXRETU+1]
Rs = [3*MAXRETU, 3*MAXRETU+1]
for i, j in zip(Gs, Gs[1:]):
    unite(i, j, table)
if ZABUTON:
    Ys = [0, 1, 2]
    for i, j in zip(Ys, Ys[1:]):
        unite(i, j, table)
i, j = Rs
unite(i, j, table)

# 111~120 要らないかも(recの中でやるので)

rec(0, 0, 0, *table)

memo()
