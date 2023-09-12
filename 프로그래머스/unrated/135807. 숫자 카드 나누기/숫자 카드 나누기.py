import math

def solution(arrayA, arrayB):
    # A
    temp = arrayA[0]
    for i in range(len(arrayA) -1) :
        temp = math.gcd(temp, arrayA[i+1])
        if temp == 1 :
            temp = 0
            break
        
    if temp != 0 :
        for k in arrayB:
            if k % temp == 0 :
                temp = 0
                break
    a = temp
    
    # B
    temp = arrayB[0]
    for i in range(len(arrayB) -1) :
        temp = math.gcd(temp, arrayB[i+1])
        if temp == 1 :
            temp = 0
            break
        
    if temp != 0 :
        for k in arrayA:
            if k % temp == 0 :
                temp = 0
                break
    b = temp
    
    return max(a,b)