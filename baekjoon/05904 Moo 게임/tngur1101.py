# Moo 수열
# Moo(n) = Moo(n-1) + "m" + "o"*(n+2) + Moo(n-1)
# 그럼 얘를 왼쪽 Moo(n-1), 오른쪽 Moo(n-1), 가운데 "m" + "o"*(n+2)로 나눠서 분할 정복 이용

N= int(input())

moo = ['m', 'o', 'o']

def Moo(n,prev_len, idx):
    moo_len = 2*prev_len + idx + 3

    if n<=3:
        print(moo[n-1])
        return
    
    if moo_len < n: # 새로운 길이가 n보다 작은 경우
        Moo(n,moo_len,idx+1)
    else:   # 새로운 길이가 n보다 큰 경우
        # 그럼 왼쪽 Moo(n-1)은 고려 x
        if n>prev_len+idx+3:
            Moo(n-(prev_len + idx + 3), 1, 3)
        elif prev_len < n and n<=prev_len+idx+3:
            if n - prev_len == 1:
                print("m")
            else:
                print("o")
            return
        
Moo(N,1,3)
