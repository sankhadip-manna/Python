a = int(input("Enetr Frist Number:"))
b = int(input("Enetr Secound Number:"))

if( b==0):
    raise ZeroDivisionError("Hey our program is not meant to dividen number by zero")
else:
 print(f"The divied a/b is {a/b}")