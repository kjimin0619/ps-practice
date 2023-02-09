import sys
def scoring(s):
    cn = 0
    totalScore = 0
    for score in s:
        if score == "O" :
            cn += 1 
        else :
            cn = 0
            
        totalScore += cn
    return totalScore
    
n = int(input())
for _ in range(n):
    s = sys.stdin.readline()
    print(scoring(s))