# Given an array of integers and a window size k, 
# find the first negative integer in every contiguous subarray (sliding window) of size k. 
# If a window contains no negative number, return 0 for that window.

arr = [-8, 2, 3, -6, 10]
k = 2

# output : [-8, 0, -6, -6]

def first_neg(arr,k):
    ans=[]

    for i in range(len(arr)-k+1):
        found=False

        for j in range(i,i+k):
            if arr[j] <0:
                ans.append(arr[j])
                found=True
                break
        if not found:
            ans.append(0)
    return ans

print(first_neg(arr,k))