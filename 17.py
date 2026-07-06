# convert string to dict 
# not imp  

s = '{"name": "John", "age": 25, "city":"Del"}'

result={}
s=s.strip("{}")

items=s.split(",")
for item in items:
    # key,value = item.split("=")
    key,value = item.split(":")
    result[key]= value
print(result)
