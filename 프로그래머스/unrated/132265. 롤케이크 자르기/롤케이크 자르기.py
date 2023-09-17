from collections import Counter
def solution(topping):
    answer = 0
    a = Counter(topping)
    b = set()
    for i in topping :
        a[i] -= 1
        if a[i] == 0 :
            del a[i]
        b.add(i)
        
        if len(b) == len(a.keys()) :
            answer += 1
            
            
    return answer