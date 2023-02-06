def solution(s):
    answer = -1
    s = list(s)
    cnt = 0
    for i in range(len(s)):
        if s[0] in ["]", "}", ")"]:
            pass
        else:
            cnt+=1
        temp = s[0]
        s[:len(s)-1] = s[1:len(s)]
        s[len(s)-1] = temp

    answer = cnt
    return answer