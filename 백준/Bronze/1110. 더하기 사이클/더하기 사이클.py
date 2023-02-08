import sys

num = sys.stdin.readline().strip()
if (len(num) == 1) : num = "0"+num
num = [int(num[0]), int(num[1])]

count = 0
newNum = num
while True :
    newA = newNum[0]
    newB = newNum[1]
    newNum = [newB, (newA+newB)%10]
    count += 1
    if (newNum[0] == num[0]) and (newNum[1] == num[1]) :
        break
    
print(count)