import sys

word = sys.stdin.readline().upper().strip() # 대문자로 변경
unique_word = list(set(word)) # 중복값 제거

cnt = []
for x in unique_word :
    cnt.append(word.count(x))
    
m = max(cnt)
if cnt.count(m) > 1 : 
    print("?")
else : 
    m_index = cnt.index(m)
    print(unique_word[m_index])