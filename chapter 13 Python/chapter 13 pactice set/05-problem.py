from functools import reduce 

s = [1223,33434,3456,324,56,87,23,25]

def greater(a,b):
    if(a>b):
        return a
    return b

print(reduce(greater,s))