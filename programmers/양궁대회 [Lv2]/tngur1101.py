from itertools import combinations_with_replacement 

def solution(n, info):
    answer = [-1]
    diff = 0
    
    score_arr = [0,1,2,3,4,5,6,7,8,9,10]
    for score in combinations_with_replacement(score_arr,n):
        lion_arr = [0 for _ in range(11)]
        
        for i in score:
            lion_arr[10-i]+=1
            
        appeach, lion = 0,0
        for idx in range(len(info)):
            if info[idx] == lion_arr[idx]==0:   # 둘다 한번도 못맞췄을 때
                continue
            elif info[idx] >= lion_arr[idx]:
                appeach += 10-idx
            else:
                lion += 10-idx
                
        if lion>appeach:
            gap = lion - appeach
            if gap>diff:
                diff = gap
                answer = lion_arr
    return answer