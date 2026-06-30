# Fibonacci 

def fibb(n):
    result=[]
    a=0
    b=1
    for i in range(n):
        result.append(a)
        temp=a
        a=b
        b=temp+b
    return result
n= int(input("enter "))

print(fibb(n))

