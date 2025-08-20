p = int(input("Enter Your Number: "))

for i in range(2, p):
    if(p%i==0):
        print("Number is not prime")
        break
else:
    print("Number is prime")