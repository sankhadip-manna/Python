class Employee:
    def __init__(self):
        # super().__init__()
        print("Constract of Employee")
    a =1
class Programer(Employee):
    def __init__(self):
        super().__init__()
        print("Constract of Programer")
    b =2
class Mangaer(Programer):
    def __init__(self):
     super().__init__()
     print("Constract of Managare")
        
    c =3

# o = Employee()
# print(o.a)
# o = Programer()
# o.b
# print(o.a,o.b)
o = Mangaer()
print(o.a,o.b,o.c)
