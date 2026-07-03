# flatten an array 

arr = [
    [100, 2],
    [3, [4,88],],
    [5, 6]
]

def flatt(arr):
    result=[]
    for item in arr:
        if isinstance(item,list):
            result.extend(flatt(item))
        else:
            result.append(item)
    return result
print(flatt(arr))
