import sys

n = int(sys.stdin.readline())
scores = list(map(int, sys.stdin.readline().split(" ")))

m = max(scores)
new_scores = [i/m *100 for i in scores]
print(sum(new_scores)/n)
