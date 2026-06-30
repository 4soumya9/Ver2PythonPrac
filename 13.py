# Max in array 

nums = [4, 2, 4, 1, 20, 5, 1]
maxx=nums[0]

for i in nums:
    if maxx < i:
        maxx =i
print(maxx)
