def solution(name):
    answer = 0
    print(name)
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
# a b c d e f g h i j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z
    # 13개 -> m전까지는 앞에서 탐색 m 이후는 z부터 탐색
    name_list = []
    for i in name:
        name_list.append(ord(i))
    joy_list = [0 for i in range(len(name))]
    joy_cnt = 0
    cnt = 0
    for index in name_list:
        if index <= 77 and index>64:
            joy_cnt += index - 65
            joy_list[cnt]=joy_cnt
            cnt+=1
            joy_cnt = 0
        elif index>77 and index<=90:
            joy_cnt += 91-index
            joy_list[cnt]=joy_cnt
            cnt+=1
            joy_cnt = 0
    sum_cnt = 0
    print(joy_list)
    sum_cnt = sum(joy_list)
    print(sum_cnt)
        
    return answer