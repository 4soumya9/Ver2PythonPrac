# Find the largest word in sentence

# sentence = ""
s = "Python is the best programming language"
words= s.split()
maxx=""

for word in words:
    if len(word) > len(maxx):
        max=word
print(maxx)

