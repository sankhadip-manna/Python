class Employee:
    langauge = "Python"
    salary = 1200000

    def __init__(self,name,salary,language): # dunder method which is automaticaly called 
        self.name = name
        self.salary = salary
        self.langauge = language
        print("I an creating an object")


    def getinfo(self):
        print(f"The Language is{self.langauge}. This salary is a {self.salary}.")

    @staticmethod
    def greet():
        print("Good Mornig.") 


sankha = Employee("Sankha",12000,"JavaScript") 
# sankha.name = "Sankah"
print(sankha.name,sankha.salary,sankha.langauge)

# subham = Employee()
