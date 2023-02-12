def solution(m, n, puddles):
    dp = [[0]*(n + 1) for _ in range(m + 1)]
    mod = 10**9 + 7

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if [i, j] == [1, 1]:
                dp[i][j] = 1
            elif [i, j] not in puddles:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % mod

    return dp[m][n]