def rotate_piece(piece):
    for a, b in [["U", "r"], ["R", "d"], ["D", "l"], ["L", "u"]]:
        piece = piece.replace(a, b)

    return piece.upper()

def dfs(i, j, no, field, visited):
    visited[i][j] = no
    dxs = [[-1, 0, "U", "D"], [1, 0, "D", "U"], [0, -1, "L", "R"], [0, 1, "R", "L"]]
    path = []

    for dx in dxs:
        ni, nj = i + dx[0], j + dx[1]

        if 0 <= ni < len(field) and 0 <= nj < len(field[0]) and not visited[ni][nj] and field[ni][nj]:
            path.append(dx[2])
            path += dfs(ni, nj, no, field, visited)
            path.append(dx[3])

    return path

def solution(game_board, table):
    n, m = len(game_board), len(game_board[0])
    visited_game_board = [[0]*55 for _ in range(55)]
    visited_table = [[0]*55 for _ in range(55)]
    game_board_pieces = []
    table_pieces = []

    for i in range(n):
        for j in range(m):
            game_board[i][j] = 1 - game_board[i][j]

    for i in range(n):
        for j in range(m):
            if not visited_game_board[i][j] and game_board[i][j]:
                no = len(game_board_pieces) + 1
                game_board_pieces.append("S" + "".join(dfs(i, j, no, game_board, visited_game_board)) + "S")

            if not visited_table[i][j] and table[i][j]:
                no = len(table_pieces) + 1
                table_pieces.append("S" + "".join(dfs(i, j, no, table, visited_table)) + "S")

    ans = 0

    while table_pieces:
        target_idx = -1

        for i in range(n):
            for j in range(m):
                if not game_board[i][j]:
                    continue

                for idx, piece in enumerate(table_pieces):
                    if target_idx != -1:
                        break

                    if len(piece) != len(game_board_pieces[visited_game_board[i][j] - 1]):
                        continue

                    for _ in range(4):
                        piece = rotate_piece(piece)

                        dx_dict = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
                        ni, nj = i, j
                        ok = True

                        for op in piece:
                            if op in dx_dict:
                                ni, nj = ni + dx_dict[op][0], nj + dx_dict[op][1]

                            if not (0 <= ni < n) or not (0 <= nj < m) or not game_board[ni][nj]:
                                ok = False
                                break

                        if ok:
                            for op in piece:
                                if op in dx_dict:
                                    ni, nj = ni + dx_dict[op][0], nj + dx_dict[op][1]

                                game_board[ni][nj] = 0

                            target_idx = idx
                            break

        if target_idx == -1:
            break

        ans += len(table_pieces[target_idx]) // 2
        table_pieces.pop(target_idx)

    return ans