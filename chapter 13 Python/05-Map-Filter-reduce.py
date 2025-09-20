from functools import reduce
# ********Map*********
l = [1,2,3,4,5]

squrae = lambda x: x*x
sqList = map(squrae,l)
print(list(sqList))

# ***********Filter Example***********

def even(n):
    if(n%2==0):
        return True
    return False

onlyEven = filter(even,l)
print(list(onlyEven))


# ********Reduce**********
def sum(a,b):
    return a*b

print(reduce(sum,l))

