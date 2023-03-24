# 이 문제가 그리디로는 안풀리는 이유
# 차례대로 주문이 들어옴 -> 문제는 이 주문을 처리할 수도 있고 안할 수도 있음...
# 동적계획법 중 냅섹 문제
# https://sweetdev.tistory.com/982  knapack(배낭 문제) 쉽게 구현하기 참고


# 4 3 4
# 치즈버거 3 감튀 4
# 주문
# 2 5 -> 불가
# 1 2
# 3 3
# 2 1


        # 0 3 4 -> 주문번호: 0 현재 남은 치즈버거: 3 현재 남은 감자튀김: 4
# 처리 하면             # 처리하지 않고 다음 주문번호를 받으면
# 1 1 -1이 됨           # 1 3 4 에서 2번째 주문 받고
            #   처리 하면       #   처리하지 않으면
            #   2 2 2가 됨      #   2 3 4
            # 3번째 주문 받으면
        # 처리시    # 처리 x    #처리시     #처리x
        # 3 -1 -1   # 3 2 2     #3 0 1      # 3 3 4
        # 4번째 주문받으면                      
                    #처리시 #처리 x         # 처리시 # 처리 x
                    #4 0 1  # 4 2 2         # 4 1 3  # 4 3 4

n,m,k = map(int, input().split())
dp = [[[0]*(k+1) for _ in range(m+1)] for _ in range(n+1)]

answer = 0

for pos in range(1,n+1):
    cheese_burger, potato_chips = map(int, input().split())

    for cheese in range(m+1):
        for potato in range(k+1):
            if cheese>=cheese_burger and potato>=potato_chips:
                dp[pos][cheese][potato] = max(1+dp[pos-1][cheese][potato], dp[pos-1][cheese][potato])
            else:
                dp[pos][cheese][potato] = dp[pos-1][cheese][potato]
            answer = dp[pos][cheese][potato]

print(answer)