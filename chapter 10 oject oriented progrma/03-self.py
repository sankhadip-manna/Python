class Employee:
    langauge = "Python"
    salary = 1200


    def getinfo(self):
        print(f"The Language is{self.langauge}. This salary is a {self.salary}.")

    @staticmethod
    def greet():
        print("Good Mornig.") 


sankha = Employee()
sankha.langauge = "JavaScript" 


sankha.greet()
sankha.getinfo()
# Employee.getinfo(sankha)