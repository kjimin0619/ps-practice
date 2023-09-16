from sys import stdin as ss
t = int(ss.readline())

for _ in range(t):
    result = 0
    temp = ss.readline().strip()
    s = 0
    e = len(temp) -1
    
    while s < e :
        sn = temp[s]
        en = temp[e]
        
        if sn == en :
            s += 1
            e -= 1
        
        else :
            # 오른쪽 문자열 제거
            if s <= e-1 :
                new_temp = temp[:e] + temp[e+1 :]
                if new_temp[:] == new_temp[::-1] :
                    result = 1
                    break
         
            # 왼쪽 문자열 제거
            if s+1 <= e :
                new_temp = temp[:s] + temp[s+1:]
                if new_temp[:] == new_temp[::-1] :
                    result = 1
                    break
                
            result = 2
            break
    
    print(result)