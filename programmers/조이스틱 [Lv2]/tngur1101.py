def solution(name):
    answer = 0
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
# a b c d e f g h i j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z
    # 13개 -> m전까지는 앞에서 탐색 m 이후는 z부터 탐색
    # 2가지 방향에서 최솟값 도출하기
    # 상하 -> A에서 시작하는게 좋은지 Z에서 시작하는게 좋은지
    # 좌우 -> 왼쪽으로 가는게 나은지 오른쪽으로 가는게 나은지
    cnt = 0
    l_r_move = len(name)-1
    for char in name:
        answer += min(ord(char) - ord("A"), ord("Z")+1-ord(char))
        
    for i in range(len(name)):
        cnt = i + 1
        while cnt < len(name) and name[cnt] == "A":
            cnt += 1
        l_r_move= min(l_r_move, i+i+len(name)-cnt)
    
    answer += l_r_move
        
    return answer