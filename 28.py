# Convert string into dict 
s="a.b.c"
s= s.split(".")
result={}
temp = result
for item in s:
    temp[item ]= {}
    temp=temp[item]

print(result)
