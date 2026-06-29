# rev with return statement  (each letter in a sentence)
s = "Hellb wor"
def revv3(s):
    result=[]
    words = s.split()
    for ch in words:
        rev =""
        for i in ch:
            rev = i+rev
        result.append(rev)
    return " ".join(result).capitalize()
print(revv3(s))

