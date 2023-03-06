def solution(numbers):
    answer = []
    # 짝수는 끝이 무조건 0으로 끝나고 가장 뒤의 0만 바꿔주면 2개 이하의 다른 비트 중 가장 작은 수가 됨
    
    # 홀수는 가장 뒤 쪽에 있는 0을 찾아서 해당 0을 1로 바꿔주고 그 다음 인덱스의 1을 0으로 바꿔주면 됨
    # 예외
    # 7 => 111로 모두 1로 이루어져 있어 앞에 0을 붙여줘야 함
    for num in numbers:
        if num%2 == 0:
            temp = list(bin(num))[2:]
            temp[-1]="1"
        else:
            temp = bin(num)[2:]
            temp = "0"+temp
            z_idx = temp.rindex("0")
            temp = list(temp)
            temp[z_idx] = "1"
            temp[z_idx+1]="0"
        a_num = int("".join(temp),2)
        answer.append(a_num)
    return answer