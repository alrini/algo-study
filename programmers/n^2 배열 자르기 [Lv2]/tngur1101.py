def solution(n, left, right):
    answer = []

    for i in range(n**2):
        a = i//n
        b = i%n
        answer.append(max(a,b)+1)

    answer = answer[left:right+1]
    return answer

# 시간초과로 인해 정확성 30.0
# 합계: 30.0 /  100.0