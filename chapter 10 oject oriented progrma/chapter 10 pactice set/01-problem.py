class programer:
    company = "Wippro"
    def __init__(self,name,salary, pin):
        self.name=name
        self.salary = salary
        self.pin = pin

p = programer("Sankha",80000,7111414)
print(p.name,p.company,p.salary,p.pin)
r = programer("Subham",80000,7111414)
print(r.name,r.company,r.salary,r.pin)
        
