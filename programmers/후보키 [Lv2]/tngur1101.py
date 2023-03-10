from itertools import combinations
def solution(relation):
    answer = 0
    r = len(relation)   #행
    c = len(relation[0])    #열
    
    comb_arr = []
    for i in range(1,c+1):
        comb_arr.extend(combinations(range(c),i))
    
    #print(comb_arr)
    unique_arr = []
    for comb in comb_arr:
        temp = [tuple([item[key] for key in comb]) for item in relation]
        #print(temp)
        
        if len(set(temp)) == r:
            candidate = True
            
            for u in unique_arr:
                if set(u).issubset(set(comb)):
                    candidate = False
                    break
            
            if candidate: 
                unique_arr.append(comb)
    answer = len(unique_arr)
    return answer