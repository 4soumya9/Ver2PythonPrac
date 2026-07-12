str1= "Hello"
str2="Hello"

freq1={}
freq2={}

for ch in str1:
    freq1[ch] = freq1.get(ch,0)+1

for ch in str2:
    freq2[ch] = freq2.get(ch,0)+1

print(freq2== freq1)