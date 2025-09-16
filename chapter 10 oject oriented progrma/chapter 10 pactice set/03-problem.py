class demo:
 a = 4


o = demo()
print(o.a) #  Prints the class attribute becase instance attribute is not present  
o.a = 0 # Intence attribute is set 
print(o.a) # Prints the intance attribute beacuse instance attribute is present
print(demo.a) # Prints the class attribute 
