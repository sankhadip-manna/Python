def disvision(n):
    if(n%5==0):
        return True
    return False

s = [1223,33434,3456,324,56,87,23,25]
f = list(filter(disvision,s))
print(f)