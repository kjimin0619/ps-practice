alp = list(range(97,123)) # a= 97, z= 122
word = input().strip()

for x in alp :
    print(word.find(chr(x))) 