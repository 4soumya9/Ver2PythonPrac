# Rev Sentence : Hello World  

s = "Hello wor" 
# op: Wor hello

def revv(s):
    result=[]
    words=s.split()

    for i in range(len(words)-1,-1,-1):
        result.append(words[i])
    return " ".join(result).capitalize()
print(revv(s))


    

