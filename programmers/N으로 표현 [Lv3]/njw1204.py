def solution(N, number):
    MAX_DIST = 8

    dist = dict()
    numsOfDist = [[] for _ in range(MAX_DIST + 1)]

    for d in range(1, MAX_DIST + 1):
        for i in range(1, d):
            j = d - i

            for a in numsOfDist[i]:
                for b in numsOfDist[j]:
                    possibles = [a + b, a - b, a * b] + ([a // b] if b != 0 else [])

                    for possible in possibles:
                        if possible not in dist:
                            dist[possible] = d
                            numsOfDist[d].append(possible)

        dist[int(str(N) * d)] = d
        numsOfDist[d].append(int(str(N) * d))

    return dist.get(number, -1)