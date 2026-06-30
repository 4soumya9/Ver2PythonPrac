# Find dup in string 

def dupp(s):
    seen = set()
    dup =set()
    for char in s:
        if char in seen:
            dup.add(char)
        else:
            seen.add(char)
    return dup
print(dupp("Hello"))

