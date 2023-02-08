import sys

totalPrice = int(sys.stdin.readline()) # 영수증에 적힌 총 금액
n = int(sys.stdin.readline()) # 물건의 종류 수

for _ in range(n):
    price, num = map(int, sys.stdin.readline().split(" "))
    totalPrice -= price * num

if totalPrice == 0 : print("Yes")
else : print("No")