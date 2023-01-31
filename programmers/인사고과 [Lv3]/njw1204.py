def solution(scores):
    scores = list(enumerate(scores))
    scores.sort(key=lambda x: (-x[1][0], x[1][1]))
    
    filtered_scores = []
    max_b = -1
    my_score = -1
    
    for i, score in scores:
        if score[1] < max_b:
            continue
        
        filtered_scores.append(score[0] + score[1])
        max_b = max(max_b, score[1])
        
        if i == 0:
            my_score = score[0] + score[1]
    
    if my_score == -1:
        return -1
    
    return len(list(filter(lambda x: x > my_score, filtered_scores))) + 1