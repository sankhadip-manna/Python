class vactor:
    def __init__(self ,i,r,z):
        self.i =i
        self.r =r
        self.z =z

        def __add__(self, other):
            result = vactor(self.i + other.i, self.r + other.r, self.z + other.z)
            return result
        
        def __mul__(self, other):
            result = self.i * other.i + self.r * other.r + self.z * other.z
            return result
        
        def __str__(self):
            return f"{self.i}i + {self.r}r + {self.z}z"
        

        v1 = vactor( 1,2,3)
        v2 = vactor( 4,6,7)
        v3 = vactor( 9,8,6) #same dimension vector

        print(v1 + v2) #vector addition
        print(v1 * v2) #dot product
        
        print(v1 + v2 + v3) #vector addition
        print(v1 * v2 * v3) #dot product
        