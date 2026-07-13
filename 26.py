# Given 2 arrays that are sorted [0,3,4,31] and [4,6,30]. 
# Merge them and sort [0,3,4,4,6,30,31] ? 

arr1 = [0, 3, 4, 31]
arr2 = [4, 6, 30]
# op: [0, 3, 4, 4, 6, 30, 31]

i=0
j=0
result=[]
while i< len(arr1) and j <len(arr2):
    if arr1[i] < arr2[j]:
        result.append(arr1[i])
        i +=1
    else:
        result.append(arr2[j])
        j+=1
while i <len(arr1):
    result.append(arr1[i])
    i+=1
while j <len(arr2):
    result.append(arr2[j])

print(result)