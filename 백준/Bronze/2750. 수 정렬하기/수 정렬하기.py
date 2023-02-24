import sys
input = sys.stdin.readline

n = int(input())

nums = [int(input()) for i in range(n)]

for num in sorted(nums) : print(num)