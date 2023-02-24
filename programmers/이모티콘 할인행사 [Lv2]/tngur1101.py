from itertools import product

def solution(users, emoticons):
    answer = [0,0]
    
    # 이모티콘 할인률 [10,20,30,40]
    n = len(emoticons)
    
    dis_rate = [10,20,30,40]
    
    for case in product(dis_rate, repeat=len(emoticons)): # 완전 탐색
        total_pay, plus_num = 0,0
        for rate, price in users:
            pay = 0
            for i,emoticon in enumerate(emoticons):
                if case[i] >= rate: # 이모티콘 할인률(case[i]가 rate보다 커서 이모티콘을 구매하는 경우)
                    pay += emoticons[i] * (100-case[i]) // 100
                else:
                    pass
            if pay >= price:    # 이모티콘 구매를 취소하고 이모티콘 플러스에 구독하는 경우
                plus_num += 1
            else:   # 이모티콘만 결제하는 경우
                total_pay += pay
                
        if plus_num > answer[0]:
            answer[0], answer[1] = plus_num, total_pay
        elif plus_num == answer[0] and total_pay > answer[1]:
            answer[1] = total_pay
            
    
    
    return answer