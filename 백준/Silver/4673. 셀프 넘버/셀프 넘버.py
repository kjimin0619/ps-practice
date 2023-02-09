def find_remove(n) :
    noneSelfNum = n
    while n != 0 :
        noneSelfNum += n % 10 # 오른쪽 숫자부터 더함
        n = n // 10
    return noneSelfNum

numbers = set(i for i in range(1,10001))
remove_numbers = set()
for n in range(1,10001) :
    remove_numbers.add(find_remove(n))

self_numbers = numbers - remove_numbers  
for selfNum in sorted(self_numbers) :
    print(selfNum)