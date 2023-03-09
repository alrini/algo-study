import math
def solution(str1, str2):
    answer = 0
    
    str1 = str1.lower()
    str2 = str2.lower()
    
    str1_arr = []
    str2_arr = []
    
    for i in range(len(str1)-1):    # 2개씩 끊어주기
        if str1[i].isalpha() and str1[i+1].isalpha():
            str1_arr.append(str1[i:i+2])
    
    for i in range(len(str2)-1):    # 2개씩 끊어주기
        if str2[i].isalpha() and str2[i+1].isalpha():
            str2_arr.append(str2[i:i+2])
    
    #print(str1_arr)
    #print(str2_arr)
    intersection_arr = set(str1_arr) & set(str2_arr)
    #print(intersection_arr)
    union_arr = set(str1_arr)|set(str2_arr)
    #print(union_arr)
    
    if len(union_arr)==0:   # 테스트 4 case 처리하기
        return 65536
    
    int_len = sum([min(str1_arr.count(intersection), str2_arr.count(intersection)) for intersection in intersection_arr])
    un_len = sum([max(str1_arr.count(union), str2_arr.count(union)) for union in union_arr])

    answer = math.floor((int_len/un_len)*65536)
    
    return answer