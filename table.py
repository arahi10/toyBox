from puyo import Puyo
from base import *


class Table:
    def __init__(self, tbl):
        self.table = [[Puyo(tbl[i][j], i, j)for j in range(MAXRETU)]
                      for i in range(MAXDAN)]

    def same_colors(self, i, j):
        ret = set()
        non_seach = {(i, j)}
        c = self.table[i][j].color
        while non_seach:
            tmp = set()
            for i, j in non_seach:
                for x, y in make_adjacent(i, j):
                    if self.table[x][y].color == c and (x, y)not in ret:
                        tmp.add((x, y))
            ret |= non_seach
            non_seach = tmp
        return ret

    def vanish(self, num):
        seen = set()
        ret = {}
        for i in range(MAXDAN-1, -1, -1):
            for j in range(MAXRETU-1, -1, -1):
                if (i, j) in seen or self.table[i][j].color is None:
                    continue
                # if i==2 and j==1:
                #     p =1
                #     pass

                connect = self.same_colors(i, j)
                seen |= connect
                if len(connect) >= 4:
                    for i, j in connect:
                        puyo = self.table[i][j]
                        ret[puyo.i, puyo.j] = num
                        self.table[i][j] = Puyo(NULL, 0, 0)
        return ret

    def drop_float_puyo(self):
        for j in range(MAXRETU):
            for i in range(MAXDAN-2, -1, -1):
                while i != MAXDAN-1 and self.table[i+1][j].color is None:
                    self.table[i+1][j] = self.table[i][j]
                    self.table[i][j] = Puyo(NULL, 0, 0)
                    i += 1

    def chain(self):
        ret = {}
        head = 1
        # ざぶとんあり
        if ZABUTON:
            for i, j in ((0, 0), (0, 1), (0, 2)):
                self.table[i][j] = Puyo(NULL, i, j)
                ret[i, j] = head
            head += 1

        for i, j in ((1, 0), (2, 0), (2, 1)):
            self.table[i][j] = Puyo(NULL, i, j)
            ret[i, j] = head
        self.drop_float_puyo()
        for num in range(head+1, RENSA+head):
            vs = self.vanish(num).items()
            if len(vs):
                for k, v in vs:
                    ret[k] = v
                self.drop_float_puyo()
            else:
                return {}
        return ret


if __name__ == '__main__':
    # test code
    s = NULL
    ZABUTON = False
    t = Table(
        [[s, s, s, s, 1, s],
         [1, 2, 3, 1, 4, 1],
         [1, 1, 2, 3, 3, 4],
         [2, 2, 3, 4, 4, 1]])
    ans = t.chain()
    print(show(ans).replace(',', '\n'))
