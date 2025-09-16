class Employee:
    a =1
class Programer(Employee):
    b =2
class Mangaer(Programer):
    c =3

o = Employee()
print(o.a)
o = Programer()
o.b
print(o.a,o.b)
o = Mangaer()
print(o.a,o.b,o.c)
