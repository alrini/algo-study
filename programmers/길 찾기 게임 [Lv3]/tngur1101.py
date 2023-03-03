def preorder(x_arr, y_arr, answer):
    node = y_arr[0] # y값이 제일 큰 애
    left_arr = []   # y_arr[0]을 중심으로 왼쪽에 있는 애들을 담을 배열
    right_arr = []  # y_arr[0]을 중심으로 오른쪽에 있는 애들을 담을 배열

    for i in range(1, len(y_arr)):
        if node[0] > y_arr[i][0]:
            left_arr.append(y_arr[i])
        else:
            right_arr.append(y_arr[i])

    if len(left_arr) > 0:
       pass # 재귀로 계속 불러와야 할 것 같은데 여기에 뭐가 들어가야할지를 모르겠음
    else:
        pass 

def postorder(x_arr, y_arr, answer):
    pass

def solution(nodeinfo):
    answer = [[]]

    preanswer = []
    postanswer = []

    x_arr = sorted(nodeinfo)
    y_arr = sorted(nodeinfo, key=lambda x: (-x[1], x[0]))

    answer = [preanswer, postanswer]

    return answer