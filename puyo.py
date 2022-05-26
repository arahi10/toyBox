from base import *

class Puyo:
    def __init__(self,col,i,j):
        self.color = col if col!=NULL else None
        self.i = i
        self.j = j
        self.number_of_chain = 0
    def __repr__(self):
        return str(self.color) if self.color is not None else "0"
