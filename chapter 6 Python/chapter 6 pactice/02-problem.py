markes1 = int(input("Enter Your Markes 1: "))
markes2 = int(input("Enter Your Markes 2: "))
markes3 = int(input("Enter Your Markes 3: "))
markes4 = int(input("Enter Your Markes 4: "))

# chack for total parcentage

total_percentage = (100*(markes1+markes2+markes3+markes4))/400

if(total_percentage>=40 and markes1>=33 and markes2>=33 and markes3>=33 and markes4>=33):
    print("You are pass",total_percentage)

else:
    print("You are failed , try again next year!",total_percentage)