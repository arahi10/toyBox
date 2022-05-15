
RED = 1
GREEN = 2
BLUE = 3
YELLOW = 4
MAXRETU = 5
MAXDAN = 4
RENSA = 5

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

def make_parent(i,j):
    if i!=0:
        yield (i-1,j)
    if j!=0:
        yield (i,j-1)