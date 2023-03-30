def solve(cur_lv, idx):
    global moo_len

    if cur_lv == 0:
        if idx == 0:
            return "m"
        else:
            return "o"

    left, mid = moo_len[cur_lv - 1], cur_lv + 3

    if idx < left:
        return solve(cur_lv - 1, idx)
    elif idx >= (left + mid):
        return solve(cur_lv - 1, idx - (left + mid))
    else:
        if idx == left:
            return "m"
        else:
            return "o"

moo_len = [0] * 30
moo_len[0] = 3

for i in range(1, 30):
    moo_len[i] = moo_len[i - 1] * 2 + i + 3

print(solve(30, int(input()) - 1))
