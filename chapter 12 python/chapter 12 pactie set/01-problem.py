
try:
    with open("one.txt", "r") as f:
        a = f.read()
        print(a)
except Exception as e:
    print(e)
try:
    with open("two.txt", "r") as f:
        a = f.read()
        print(a)
except Exception as e:
    print(e)
    
try:
    with open("three.txt", "r") as f:
        a = f.read()
        print(a)
except Exception as e:
    print(e)