n = int(input())
def draw(n):
    if (n == 1) :
        return ["*"]
    Stars = draw(n//3)
    L = []
    
    # 첫 번째 줄
    for star in Stars:
        L.append(star*3)
    
    # 두 번째 줄
    for star in Stars :
        L.append(star+' '*(n//3)+star)

    # 세 번째 줄
    for star in Stars :
        L.append(star*3)

    return L

# result = draw(n)
# print('\n'.join(result))

[print(i) for i in draw(n)]