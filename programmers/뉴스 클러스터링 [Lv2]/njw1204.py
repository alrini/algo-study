def solution(str1, str2):
    strs = [str1.upper(), str2.upper()]
    tokens = [dict(), dict()]

    for i in range(2):
        for j in range(len(strs[i]) - 1):
            token = strs[i][j:j+2]

            if not all("A" <= c <= "Z" for c in token):
                continue

            tokens[i][token] = tokens[i].get(token, 0) + 1

    union_size = 0
    intersect_size = 0

    for token in [token for token in tokens[0] if token in tokens[1]]:
        union_size += max(tokens[0][token], tokens[1][token])
        intersect_size += min(tokens[0][token], tokens[1][token])

    for token in [token for token in tokens[0] if token not in tokens[1]]:
        union_size += tokens[0][token]

    for token in [token for token in tokens[1] if token not in tokens[0]]:
        union_size += tokens[1][token]

    return intersect_size * 65536 // union_size if union_size else 65536
