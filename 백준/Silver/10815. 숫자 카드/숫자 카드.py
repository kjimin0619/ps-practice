from sys import stdin as s
n = int(s.readline().strip())
cards = list(map(int, s.readline().split()))
m = int(s.readline().strip())
targets = list(map(int, s.readline().split()))

cards.sort()

for t in targets :
    low, high = 0, n-1
    exist = 0
    
    while low <= high :
        mid = (low + high) // 2
        if cards[mid] > t :
            high = mid - 1
        elif cards[mid] < t :
            low = mid + 1
        else :
            exist = 1
            break
    print(exist, end = " ")