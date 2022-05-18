from __future__ import annotations
DEBUG  = 1
class StaticPuyo:
    def __init__(self, i=-1,j=-1,col=0):
        self.parent: StaticPuyo = None #直近で連結した相手
        self.bpar: StaticPuyo = None #一つ前の親
        self.bbpar: StaticPuyo = None #二つ前の親
        #消えない＝4連結以上にならない盤面を構築したいので親は高々2回しか更新されない
        self.childA: StaticPuyo = None #自身を親とする子のぷよ
        self.childB: StaticPuyo = None
        self.size = int(col != 0)
        self.color = col
        self.i = i
        self.j = j
    #unionfindみたくサイズは親に計算を委譲
    def getsize(self):
        return self.size if self.parent is None else self.parent.getsize()

    def getparent(self):
        return self if self.parent is None else self.parent.getparent()
    #親の履歴を更新、newparを現在の親とする
    def pushpar(self, newpar: StaticPuyo):
        self.bbpar = self.bpar
        self.bpar = self.parent
        self.parent = newpar

    def poppar(self):
        self.parent = self.bpar
        self.bpar = self.bbpar
        self.bbpar = None
    #unionfindと同じ
    def is_connected(self, other: StaticPuyo):
        return self.getparent() == other.getparent()
    #消えることなく連結できるならTrue,そうでなければ連結の更新を行わずFalse
    def touchWithoutVanish(self, other: StaticPuyo):
        # update size,push par
        if self.is_connected(other) or other.color != self.color:
            return True
        if self.getsize() + other.getsize() >= 4:
            return False
        self.size += other.getsize()
        if other.parent is None:
            other.pushpar(self)
        else:
            other.getparent().pushpar(self)
            other.pushpar(self)
        if (self.childA == None):
            self.childA = other
        else:
            self.childB = other
        return True
    #連結を話す、親の更新を子に対して行う(はず)
    def disconnect(self) :
        if self.childA is not  None:
            self.childA.poppar()
        if self.childB is not None:
            self.childB.poppar()
    #以下printデバッグ用
    def __repr__(self) :
        return  self.detail() if DEBUG else self.self.color.__repr__()
    def strij(self):
        if self.i!=-1 and self.j!=-1:
            return f"{self.i},{self.j}"
        else:
            return "*,*"
    def getdetailijs(self):
        ret = "P"+self.getparent().strij()
        if self.bpar is not None :
            ret += "b"+self.bpar.strij()
        if self.bbpar is not None :
            ret+="c"+ self.bbpar.strij()
        if self.childA is not None :
            ret += "kA"+self.childA.strij()
        if self.childB is not None :
            ret += "kB"+self.childB.strij()
        
        return ret
    def detail(self):
        v=self.getsize()
        s= " RGBY"[self.color]
        return  f"c{s}s{v}i"+self.getdetailijs()

    def __str__(self) :
        ret = str(self.getsize())
        return ret
