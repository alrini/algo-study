import heapq

def solution(scoville, K):
    answer = 0
    # heapq 사용법
    # 1.item을 heap에 추가하는 법
    # heapq.heappush(heap, item)
    # 2. heap에서 가장 작은 원소를 pop
    # heapq.heappop(heap)
    # 3. 기존의 list를 즉각적으로 heap으로 변환
    # heapq.heapify
    
    heapq.heapify(scoville)
    while scoville[0]<K:
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        scov = a+b*2
        heapq.heappush(scoville, scov)
        answer += 1
    
    return answer

# 정확성: 65.4
# 효율성: 19.2
# 합계: 84.6 / 100.0