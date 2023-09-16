from sys import stdin as ss
n = int(ss.readline()) # 문자열의 길이

str = ""
for _ in range(n):
    str = str + ss.readline().strip()

# t 만들기
s = 0
e = len(str) - 1
new_str = ""
while s <= e :
    if str[s] < str[e] :
        new_str = new_str + str[s]
        s += 1
    elif str[s] > str[e] :
        new_str = new_str + str[e]
        e -= 1
    else :
        # 앞 뒤 문자가 같은 경우
        s_ = s
        e_ = e
        dff = False
        
        while s_ <= e_ :
            if str[s_] < str[e_] :
                new_str += str[s]
                s += 1
                dff = True
                break
            elif str[s_] > str[e_] :
                new_str += str[e]
                e -= 1
                dff = True
                break
            else :
                s_ += 1
                e_ -= 1
        
        if not dff :
            new_str += str[s]
            s += 1
                
for i in range(n) :
    print(new_str[i], end="")
    i += 1
    if (i%80 == 0) :
        print()

    