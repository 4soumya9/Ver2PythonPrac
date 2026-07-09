# Rev each word in sentence , that is each letter 
s = "Hellb wor" 
# output : Blleh Row 
def revw(s):
    sen =s.split()
    for word in sen:
        rev =""
        for ch in word:
            rev = ch+rev
        print(rev.capitalize(),end=" ")
revw(s)