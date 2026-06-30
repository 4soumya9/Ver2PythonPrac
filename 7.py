# Max consequtive ones 

def findd(arr):
    count=0
    maxi=0
    for i in arr:
        if i == 1:
            count+=1
            maxi= max(maxi,count)
        else:
            count=0


    return maxi

print(findd([1,1,0,80,1,1,1,1,0]))