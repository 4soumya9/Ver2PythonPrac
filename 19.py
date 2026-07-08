# Find most freq element 

nums=[1,1,1,8.8,8,2,9,8]

freq={}

for i in nums:
    freq[i]= freq.get(i,0)+1
print(max(freq,key=freq.get))