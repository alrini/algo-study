import copy

def rotate(table):
    n = len(table)
    rotated_table = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rotated_table[j][n-i-1] = table[i][j]

def dfs(board, x, y, position, n, num):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    result = [position]

    board[x][y] = 2  # 방문처리

    for i in range(4):
        px = x + dx[i]
        py = y + dy[i]

        if 0 <= px and px < n and 0 <= py and py < n:
            if board[px][py] == num:
                result += dfs(board, px, py, [position[0] + dx[i], position[1] + dy[i]], n, num)

    return result

def solution(game_board, table):
    answer = 0
    n = len(game_board)
    blank = []

    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0:
                blank.append(dfs(game_board,i,j,[0,0],n,0))

    for k in range(4):
        table = rotate(table)
        copy_table = copy.deepcopy(table)
        for i in range(n):
            for j in range(n):
                if copy_table[i][j] == 1:
                    block = dfs(copy_table, i, j, [0,0], n, 1)
                    if block in blank:
                        blank.remove(block)
                        answer += len(block)
                        table = copy.deepcopy(copy_table)
                    else:
                        copy_table = copy.deepcopy(table)

    return answer