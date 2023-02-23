def solution(name):
    cnt = 0
    answer = 0
    # 기본적인 왼쪽에서 오른쪽으로 움직이는 횟수
    l_r_move = len(name)-1

    for idx, char in enumerate(name):
        # 각 문자마다 움직이는 횟수
        answer += min(ord(char) - ord("A"), ord("Z")+1 - ord(char))
        
        # 각 알파벳 이후 연속된 A 문자열의 다음 인덱스 찾기
        cnt = idx + 1
        while cnt < len(name) and name[cnt] == "A":
            cnt += 1

        # B B A A B B B
        # A A B B A C B    
        l_r_move = min([l_r_move, idx+idx+(len(name) - cnt), idx + 2*(len(name)-cnt)])
    
    answer += l_r_move
    return answer