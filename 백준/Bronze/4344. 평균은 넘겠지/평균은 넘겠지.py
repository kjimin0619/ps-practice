import sys
c = int(input())

for _ in range(c):
    nums = list(map(int, sys.stdin.readline().split()))
    avg = sum(nums[1:])/nums[0]
    cnt = 0
    
    for score in nums[1:] :
        if score > avg : 
            cnt +=1 
    print("{:.3f}%".format(100 * cnt/nums[0]))
    