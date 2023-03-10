def rotate(arr):    # 회전 함수
    n = len(arr)
    new_key = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            new_key[j][n-i-1] = arr[i][j]
    return new_key

def check(sx,sy, key, lock, size, start, end):  # 자물쇠가 열리는지 확인하는 함수
    c_arr = [[0] * size for _ in range(size)]

    
    for i in range(len(key)):
        for j in range(len(key)):
            c_arr[sx + i][sy + j] += key[i][j]

    
    for i in range(start, end):
        for j in range(start, end):
            c_arr[i][j] += lock[i - start][j - start]
            if c_arr[i][j] != 1:
                return False

    return True


def solution(key, lock):
    answer = True
    
    start = len(key)-1
    end = start + len(lock)
    size = len(lock)+2*start
    
    for a in range(0, 4):
        for i in range(end):
            for j in range(end):
                if check(i, j, key, lock, size, start, end):
                    return True
        key = rotate(key)

    return False