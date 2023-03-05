import copy

def rotate_key(key):
    m = len(key)
    new_key = [[0] * m for _ in range(m)]

    for i in range(m):
        for j in range(m):
            new_key[i][j] = key[m - 1 - j][i]

    return new_key

def solution(key, lock):
    m = len(key)
    n = len(lock)

    for r in range(4):
        for si in range(-m + 1, n):
            for sj in range(-m + 1, n):
                ok = True
                temp_lock = copy.deepcopy(lock)

                for i in range(si, si + m):
                    for j in range(sj, sj + m):
                        if not (0 <= i < n) or not (0 <= j < n):
                            continue

                        if temp_lock[i][j] and key[i - si][j - sj]:
                            ok = False

                        temp_lock[i][j] |= key[i - si][j - sj]

                if any(any(x == 0 for x in temp_lock_row) for temp_lock_row in temp_lock):
                    ok = False

                if ok:
                    return True

        key = rotate_key(key)

    return False
