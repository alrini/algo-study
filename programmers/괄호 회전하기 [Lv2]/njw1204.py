def solution(s):
    s = list(s)
    ans = 0
    
    for _ in range(len(s)):
        stack = []
        ok = True
        
        for i in range(len(s)):
            if s[i] in "([{":
                stack.append(s[i])
            else:
                if not stack or stack[-1] != {")": "(", "]": "[", "}": "{"}[s[i]]:
                    ok = False
                    break
                
                stack.pop()
        
        if ok and not stack:
            ans += 1
        
        s.append(s[0])
        s.pop(0)
    
    return ans