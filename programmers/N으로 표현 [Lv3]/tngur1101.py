def solution(N, number):
    answer = -1 
    #각 연산들을 배열에 넣고
    #숫자와 조합
    #dp 문제
    # dp는 이전값이 다음값에 영향을 주는 문제
    dp = []
    
    for i in range(1,9):#i는 N의 개수
        case = set()
        number_case = 10*i + N
        case.add(number_case)
        # 이렇게 하면 case에는 {N}, {NN}, {NNN} 이런식으로 들어가게 됨
        
        for j in range(0,i-1):
            for m in dp[j]:
                for n in dp[-j-1]:
                    case.add(m - n)
                    case.add(m + n)
                    case.add(m * n)
                    if n != 0:
                        case.add(m // n)
                        
        if number in case:
            answer = i
            break
        
        dp.append(case)
        
    return answer