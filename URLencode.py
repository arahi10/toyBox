from itertools import product
from operator import itemgetter
from table import *
from tqdm import tqdm
url_head = r"http://www.puyop.com/s/"
encode_char = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ[]'


cushion_puyo = 7


def encode_to_URL(table: 'list[list[int]]'):
    return ''.join([url_head]+[encode_char[(o << 3)+e]for l in table for o, e in zip(l[::2], l[1::2])])


def result_to_raw_chain_table(str_table: 'list[str]'):
    ret = [list(map(int, iter(r.rstrip())))for r in str_table]
    for row_i, row in enumerate(ret):
        for i in range(len(row)):
            if row[i] == 0:
                if row_i != 0 and ret[row_i-1][i] != 0:
                    row[i] = cushion_puyo
    ret[0][1] = 0
    return ret

def translate_chain(chain,trans):
    return [[trans.get(v,v)for v in inner]for inner in chain]

def has_cushion(chain: 'list[list[int]]'):
    return any(cushion_puyo in row for row in chain)

def cushion_search(chain: 'list[list[int]]'):
    for i,L in enumerate(chain):
        for j,color in enumerate(L):
            if color == cushion_puyo:
                yield (i,j) 

def is_valid_chain(chain_table: 'list[list[int]]',cushion_indexes = set()):
    if not (ret := set(Table(chain_table).chain().keys())):
        return False
    return not (ret & cushion_indexes)



if __name__ == '__main__':
    with open("all.txt", 'r') as file:
        L = file.readlines()
    num = len(L)//(1+MAXDAN+1)
    URLs = {}
    NGs = []
    base_dict = {1:1,2:2}
    translates = []
    for i in product([3,1,2,4],[4,2,1,3],[1,3,2,4]):
        add_dict = {j:i[j-3] for j in range(3,(RENSA+1 if ZABUTON else RENSA)+1)}
        translates.append({**base_dict,**add_dict})
    def make_params(dic:dict):
        _,V = zip(*sorted(dic.items()))
        V = list(V)
        return (-len(set(dic.keys())),-sum((i-j)**2 for i,j in zip(V,V[1:])))
    translates.sort(key=make_params)
    head = 0
    for index in tqdm(range(num)):
        raw_chain = result_to_raw_chain_table(L[head+1:head+1+MAXDAN])
        c_ijs = list(cushion_search(raw_chain))

        if has_cushion(raw_chain):
            for trans in translates:
                ans = translate_chain(raw_chain,trans)
                for cols in product(range(RED,YELLOW+1),repeat=len(c_ijs)):
                    for (i,j),col in zip(c_ijs,cols):
                        ans[i][j] = col
                    if is_valid_chain(ans,set(c_ijs)):
                        URLs[index] = encode_to_URL(ans)
                        break
                else:
                    continue
                break
            else:
                NGs.append((0,index))
        else:
            for trans in translates:
                ans = translate_chain(raw_chain,trans)
                if Table(ans).chain():
                    URLs[index] = encode_to_URL(ans)
                    break
            else:
                NGs.append((1,index))

        head += 1+MAXDAN+1
    with open("urls.txt",'w') as file:
        for k,v in sorted(URLs.items(),key = itemgetter(0)):
            file.write(f"{k}:{v}\n")
    with open("urls.NGs.txt",'w')as file:
        NGs.sort()
        file.write('\n'.join(map(str,NGs)))