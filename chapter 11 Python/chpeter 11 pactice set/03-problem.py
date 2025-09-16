class Employee:
   salary = 234
   incement = 20

   @property
   def salaryAfterIncerment(self):
     return (self.salary+self.incement *(self.incement/100))
     
     
   @salaryAfterIncerment.setter
   def increment(self, salary):
      self.incement = ((salary/self.salary)-1)*100
      

e = Employee()
# print(e.salaryAfterIncerment)
e.increment=238.0
print(e.incement)