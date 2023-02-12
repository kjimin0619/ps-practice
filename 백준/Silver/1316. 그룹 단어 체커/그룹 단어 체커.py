import sys

num = int(input())
grpCnt = num
for _ in range(num):
    words = sys.stdin.readline().strip()
    wordCnt = ''
    for w in words : # 그룹 단어 체크
        if w in wordCnt and wordCnt[-1] != w :
            grpCnt -= 1
            break
        wordCnt += w
            
print(grpCnt)