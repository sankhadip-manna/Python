a = int(input("Enter a Number: "))


table = [a*i for i in range(1,11)]
with open("Table.txt","a") as f:
    f.write(f"Table is a {a}:{str(table)}\n")