a = int(input("Enter Your Age: "))

# if 1st statement
if(a%2==0):
    print("Even")

else:
    print("odd")

# End of if statement no :1

    # if 2nd statement
if(a>18):
    print("You are above the age of consent")
    print("Good Luck for you")

elif(a<0):
    print("You are entering an invailled age")
    print("Place cheak our age")


elif(a==0):
    print("You are Enter age is wrong")

else:
    print("You are below the age of consent")

# End of if statement no :2

print("Program End")