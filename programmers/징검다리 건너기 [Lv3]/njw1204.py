from collections import deque

def solution(stones, k):
    ans = 10 ** 9
    window_size = 0
    window_dq = deque()

    for i in range(len(stones)):
        while window_dq and stones[window_dq[-1]] < stones[i]:
            window_dq.pop()

        window_dq.append(i)

        if window_size < k:
            window_size += 1
        else:
            if window_dq[0] ==  i - window_size:
                window_dq.popleft()

        if window_size == k:
            ans = min(ans, stones[window_dq[0]])

    return ans