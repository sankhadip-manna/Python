import random 
n = random.randint(1,100)
a = -1
Guss = 0
while(a != n):
    Guss = int(input("Enter Your Guess a Number:- "))
    if (a == n):
        print("Lower Number Place ")
        Guss += 1
    elif(a<n):
        print("Higher Number Place")
        Guss +=1

print(f"You have guess  the Number {n} currectly in {Guss} attemts ")
