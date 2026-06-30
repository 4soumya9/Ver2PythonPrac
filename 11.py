# Palindrome 
s=str(input("ENter")).lower()
def is_pal(s):
    left =0
    right = len(s)-1

    while left< right:
        if s[left] != s[right]:
            return False
        left +=1
        right -=1
    return True

if is_pal(s):
    print("Palindrome")
else:
    print("not Palindrome")

