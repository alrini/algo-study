def solution(n, info):
    ans = [-1]
    ans_val = 0

    for case in range(2 ** 10):
        tans = [0] * 11

        for point in range(1, 11):
            if case & 1:
                tans[10 - point] = info[10 - point] + 1

            case >>= 1

        if sum(tans) > n:
            continue

        tans[-1] += n - sum(tans)
        tans_val = 0

        for point in range(11):
            if tans[10 - point] > info[10 - point]:
                tans_val += point
            elif info[10 - point]:
                tans_val -= point

        if tans_val <= 0:
            continue

        if tans_val > ans_val:
            ans = tans
            ans_val = tans_val
        elif tans_val == ans_val and tans[::-1] > ans[::-1]:
            ans = tans

    return ans