def solution(s):
    answer = -1

    stack = []
    cnt = 0
    
    for i in s:
        stack.append(i)
        
        if len(stack)>=2 and stack[-1]==stack[-2]:
            stack.pop()
            stack.pop()  
        
    if len(stack)==0:
        answer = 1
    else:
        answer = 0
    return answer