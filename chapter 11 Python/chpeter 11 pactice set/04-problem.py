class Complx:
    def __init__(self,r,i):
        self .r = r
        self .i = i

    def __add__(self,c2):
        return Complx(self.r + c2.r, self.i + c2.i)
    
    def __str__(self):
        return f"{self.r} + {self.i}"
    


c1 = Complx(1,2)
c2 = Complx(3 ,4)
print(c1 + c2)