def check_symmetry(s):
    stack = []
    
    for bracket in s:
        if bracket in ("[", "(", "{"):
            stack.append(bracket)
        else:
            if not stack:
                return False
            word = stack.pop()
            if bracket == ")" and word != "(":
                return False
            elif bracket == "]" and word != "[":
                return False
            elif bracket == "}" and word != "{":
                return False
            
    if stack:
        return False
    return True
            
    

def solution(s):
    answer = -1
    cnt = 0
    for i in range(len(s)):
        #회전처리
        m = s[:i]   #i전까지 slicing
        n = s[i:]   #i부터 slicing
        
        if check_symmetry(n+m):
            cnt += 1
    answer = cnt
    
    
    return answer