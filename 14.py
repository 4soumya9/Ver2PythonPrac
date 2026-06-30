# Find Fac 

def Fact(n):
    result =1
    for i in range(1,n+1):
        result *=i
    return result 

print(Fact(3))