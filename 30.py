# Kadane Algo 
# arr = [-2, 1, -3, 4, -1, 2]
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# op : 6
def kadane(arr):
    current_sum=arr[0]
    max_sume=arr[0]

    for i in range(1,len(arr)):
        current_sum=max(arr[i],current_sum+arr[i])
        max_sume= max(current_sum,max_sume)
    return max_sume

print(kadane(arr))