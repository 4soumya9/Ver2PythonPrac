# Find a max in Nested array  
arr = [
    [100, 2],
    [3, [4,88],],
    [5, 6]
]


def ne(arr):
    maximum = float('-inf')

    for item in arr:
        if isinstance(item,list):
            maximum=max(maximum,ne(item))
        else:
            maximum=max(maximum,item)
    return maximum
print(ne(arr))
