import sys

word = sys.stdin.readline().upper().strip() # 대문자로 변경
alpha = list(range(65,91)) # A : 65, Z : 90
cnt = [0]*26

for w in word: cnt[ord(w)%65]+=1
m = max(cnt)
if cnt.count(m) > 1 : print("?")
else : print(chr(alpha[cnt.index(m)]))