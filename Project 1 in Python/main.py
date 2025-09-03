import random
'''
1 for sanke
-1 for water
0 for gun
'''
computer = random.choice([-1,0,1])
youstr = input("Entre Your Choice: ")
youDict = {"s":1,"w":-1, "g":0}
reverseDict = {1: "Sanke", -1:"Water", 0:"Gun"}
you = youDict[youstr]

print(f"You Choice {reverseDict[you]}\nComputer Choice {reverseDict[computer]}")

if (computer == you):
    print("It is a Draw")

else:
    if(computer ==-1 and you == 1):
        print("You Win!")
    elif(computer == -1 and you == 0):
        print("You  are Loss")
    elif(computer == 1 and you == 0):
        print("You are Win")
    elif(computer == -1 and you == 1):
        print(" You are Loss")
    elif(computer == 0 and you == 1):
        print("You are Loss")
    elif(computer == 0 and   you == -1):
        print("You are Win")
    elif(computer == 1 and you == -1):
        print("You are Loss.")
    else:
        print("Wrong Choice!.Place Try again.")