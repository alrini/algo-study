def solution(places):
    ans = []

    for place in places:
        dist = [[10**9]*25 for _ in range(25)]

        for n in range(25):
            i, j = n // 5, n % 5

            if place[i][j] == "X":
                continue

            for dx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                ni, nj = i + dx[0], j + dx[1]

                if 0 <= ni <= 4 and 0 <= nj <= 4 and place[ni][nj] != "X":
                    dist[i * 5 + j][ni * 5 + nj] = 1

        for i in range(25):
            for j in range(25):
                for k in range(25):
                    dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])

        ok = True

        for i in range(25):
            for j in range(25):
                if i == j:
                    continue

                if place[i // 5][i % 5] == place[j // 5][j % 5] == "P" and dist[i][j] <= 2:
                    ok = False

        ans.append(int(ok))

    return ans