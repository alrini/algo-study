def solution(m, n, puddles):
    answer = 0
    dp = [[0]*(n+1) for i in range(m+1)]    #dp 초기화
    dp[1][1] = 1
    
    for i in range(1,m+1):  #i는 행
        for j in range(1,n+1):  #j는 열
            if i == 1 and j == 1:
                continue
            if [i,j] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i-1][j]+dp[i][j-1])%1000000007
    
    
    return dp[m][n]