class TwoDVector:
   def __init__(self, i , j):
    self.i = i
    self.j = j
   def show(self):
    print(f"The vactor{self.i} i + {self.j} j")




class ThreeDVfactor(TwoDVector):
  def __init__(self, i,j,k):
    super().__init__(i,j)
    self.k = k
  def show(self):
    print(f"The vactor is {self.i} i + {self.j} j +{self.k} k") 


o = TwoDVector(1,2)
o.show()
b   = ThreeDVfactor(1,2,3)
b.show()
    