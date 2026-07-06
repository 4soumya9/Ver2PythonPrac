# process('a3b1C2x') => ('abCx',6)
s='a3b1C2x'
def process(s):
    letters=[]
    total =0
    for ch in s:
        if ch.isalpha():
            letters.append(ch)
        else:
            total += int(ch)
    letters.sort(key=str.lower)

    return "".join(letters),total
print(process(s))
