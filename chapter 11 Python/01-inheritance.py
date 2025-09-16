class Employee:
    company = "ITC"
    def show(self):
        print(f"The name {self.name} and salary is {self.salary}")


# class Programer:
#     Comapny = "ITC Infotech"
#     def show(self):
#         print(f"The name{self.name} and salary is a {self.salary}")
    
    
#     def showLnagauge(self):
#         print(f"The name{self.name} and salary is a {self.language} Language")


class Programer(Employee):
    Company = "ITC Infotech"
    def showLnagauge(self):
        print(f"The name{self.name} and salary is a {self.language} Language")

   
        
a = Employee()

b = Programer()
print(a.company,b.Company)
