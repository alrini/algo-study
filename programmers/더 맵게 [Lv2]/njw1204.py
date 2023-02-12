import heapq

def solution(scoville, K):
    ans = 0
    heapq.heapify(scoville)

    while scoville[0] < K and len(scoville) >= 2:
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + b * 2)
        ans += 1

    return ans if scoville[0] >= K else -1