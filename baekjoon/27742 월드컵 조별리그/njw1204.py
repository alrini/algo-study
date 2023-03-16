t, k = map(int, input().split())
result = [[0] * 4 for _ in range(4)]
test_pos = [-1, -1]

for i in range(4):
    for j, x in enumerate(map(int, input().split())):
        result[i][j] = x

        if x == -1:
            test_pos = [i, j]

left, right = 0, 10**18

while left < right:
    mid = (left + right) // 2
    result[test_pos[0]][test_pos[1]] = mid
    scores = [[0, 0, 0, 0] for _ in range(4)]

    for i in range(4):
        scores[i][3] = -(i + 1)

        for j in range(i + 1, 4):
            scores[i][1] += result[i][j] - result[j][i]
            scores[i][2] += result[i][j]
            scores[j][1] += result[j][i] - result[i][j]
            scores[j][2] += result[j][i]

            if result[i][j] > result[j][i]:
                scores[i][0] += 3
            elif result[j][i] > result[i][j]:
                scores[j][0] += 3
            else:
                scores[i][0] += 1
                scores[j][0] += 1

    scores.sort(reverse=True)

    if scores[0][3] == -t or scores[1][3] == -t:
        right = mid
    else:
        left = mid + 1

print(left if left <= k else -1)
