import sys
testCase = int(input())

for _ in range(testCase) :
    cnt, word = sys.stdin.readline().split()
    for w in word : print(w*int(cnt), end='')
    print()