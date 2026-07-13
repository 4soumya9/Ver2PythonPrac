# Given two arrays arr1 and arr2, return True if every value in arr1 has its corresponding squared value in arr2, and the frequency of values is the same.

# Example 1

arr1 = [1, 2, 2]
arr2 = [1, 4, 4]

# Output: True

from collections import Counter

def same (arr1,arr2):
    return Counter(x*x for x in arr1) == Counter(arr2)

print(same([1,2,2], [1,74,4]))