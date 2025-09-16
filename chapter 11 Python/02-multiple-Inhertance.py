class Employee:
    company = "ITC"
    salary = 12000
    def show(self,):
        print(f"The name  {self.company} and salary is {self.salary}")

class coder:
    language = "Pyhton"
    def printLanguage(self):
        print(f" out of all the implemant of all coder Same Lnaguage : {self.language}")


class Programer(Employee,coder):
    Company = "ITC Infotech"
    def showLnagauge(self):
        print(f"The name {self.Company} and program is a {self.language} Language")

   
        
a = Employee()

b = Programer()
# print(a.company,b.Company)
b.showLnagauge()
b.show()
b.printLanguage()
