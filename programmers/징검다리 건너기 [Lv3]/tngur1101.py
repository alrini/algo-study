def solution(stones, k):
    answer = 0
    left = 0
    right = 200000000
    
    while left<=right:
        arr = stones
        mid = (left+right)//2
        cnt = 0
        for idx in arr:
            if idx - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        if cnt >= k:
            right = mid -1
        else:
            left = mid + 1
        
    answer = left
    return answer