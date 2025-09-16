class calaulatot:
    def __init__(self,n):
        self.n =n
    def square(self):
        print(f"The Square is {self.n*self.n}")
    def Route(self):
        print(f"The Route is {self.n**1/2}")
    def Cube(self):
        print(f"The Cube is {self.n*self.n*self.n}")

    @staticmethod
    def hello():
     print("Hello World")
        

a = calaulatot(4)
a.square()
a.Route()
a.Cube()

a.hello()
        