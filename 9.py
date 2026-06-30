# Remove dup while preserving the order
nums = [4, 2, 4, 1, 2, 5, 1]

def remm(arr):
    seen = set()
    result=[]
    for item in arr:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
print(remm(nums))
