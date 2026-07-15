# Sum of third Number 
s=[1,7,8,71,87,2]

# output : 1+71=72
def sumT(s):
    total =0
    for i in range(0,len(s),3):
        total += s[i]
    return total

print(sumT(s))

