def solution(s):
    result = []

    for i in s:
        result.append(i)

        if len(result) >= 2 and result[-2] == result[-1]:
            result.pop()
            result.pop()

    return int(not result)