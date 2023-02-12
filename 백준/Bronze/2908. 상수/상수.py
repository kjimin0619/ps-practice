import sys

words = sys.stdin.readline().split()
words[0] = words[0][::-1]
words[1] = words[1][::-1]
print(max(map(int, words)))
