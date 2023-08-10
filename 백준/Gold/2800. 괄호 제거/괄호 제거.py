from itertools import combinations

original = list(input().strip())
answer = set()
stack = [] # (
temp = [] # )

# 괄호 위치 정보 저장
for idx, word in enumerate(original):
    if word == "(" :
        stack.append(idx)
    elif word == ")":
        pair = stack.pop()
        temp.append((pair, idx))

# 괄호쌍 가지고 만들 수 있는 모든 조합
for i in range(1,len(temp)+1):
    c = list(combinations(temp, i))
    
    for combi in c :
        newString = original[:]
        for s,e in combi:
            newString[s] = ""
            newString[e] = ""
        answer.add("".join(newString))
        
answer = sorted(list(answer))
print(*answer)