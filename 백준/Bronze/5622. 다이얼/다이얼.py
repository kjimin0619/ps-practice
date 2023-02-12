word = input().strip()
time = 0

numbers = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
for w in word :
    for n in numbers :
        if w in n :
            time+=numbers.index(n)+3
print(time)

