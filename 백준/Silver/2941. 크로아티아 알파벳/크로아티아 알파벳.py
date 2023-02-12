cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']
word = input().strip()

# 크로아티아 문자 '*'로 변경
for v in cro:
    word = word.replace(v, '*')
        
print(len(word))