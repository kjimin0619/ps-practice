m = int(input())

for i in range(2,m+1):
    if m % i == 0 :
        while (m % i == 0):
            print(i)
            m = m // i