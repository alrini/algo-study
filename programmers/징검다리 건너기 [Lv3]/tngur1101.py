def solution(stones, k):
    answer = 0
    while(True):
        answer += 1
        for i in range(lne(stones)):
            if stones[i]==0:
                continue
            else:
                stones[i]-=1

            count = 0
            for stone in stones:
                if stone == 0:
                    count += 1
                    if count == k:
                        return answer
                else:
                    count = 0