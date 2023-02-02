def solution(scores):
    
    scores.sort(key=lambda x: (-x[0], x[1]))    # x[0]에 대해 내림차순으로 먼저 정렬하고, 그 안에서 x[1]에 대해 오름차순으로 정렬

    wonho = scores[0]   
    wonho_score = sum(scores[0])    # 만약 두 점수가 다 낮지 않을 시, 두 점수의 합으로 계산하기 때문에 sum으로 점수 더해주기
    answer = 1  #석차는 기본적으로 1부터 시작하기 때문에 1로 설정

    for score in scores:    #scores 돌아주면서  scores: [[3,2], [3,2], [2,1], [2,2], [1,4]]
        if wonho[0]<score[0] and wonho[1]<score[1]:     # 근무 태도 점수와 동료 평가 점수가 모두 낮은 경우 => 즉 인센티브를 받을 수 없는 경우
            return -1
        if wonho_score<score[0] + score[1]:
            answer+=1

    return answer