n, mc, mp = map(int, input().split())
dp = [[[0]*305 for i in range(305)] for j in range(105)]
ans = 0

for i in range(1, n + 1):
    cheese, potato = map(int, input().split())

    for j in range(mc + 1):
        for k in range(mp + 1):
            if j >= cheese and k >= potato:
                dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][j - cheese][k - potato] + 1)
            else:
                dp[i][j][k] = dp[i - 1][j][k]

            ans = max(ans, dp[i][j][k])

print(ans)
