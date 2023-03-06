nodes = [0] * 1024

def build_dfs(node, cur_height, max_height, target_bits):
    if cur_height == max_height:
        nodes[node] = target_bits[-1]
        target_bits.pop()
        return

    build_dfs(node * 2, cur_height + 1, max_height, target_bits)

    nodes[node] = target_bits[-1]
    target_bits.pop()

    build_dfs(node * 2 + 1, cur_height + 1, max_height, target_bits)

def checker_dfs(node, cur_height, max_height):
    if cur_height == max_height:
        return nodes[node]

    ret = max(
        checker_dfs(node * 2, cur_height + 1, max_height),
        checker_dfs(node * 2 + 1, cur_height + 1, max_height)
    )

    if ret == 1 and not nodes[node]:
        return 2

    return max(ret, nodes[node])

def solution(numbers):
    ans = []

    for number in numbers:
        bits = []
        i = number

        while i:
            bits.append(i & 1)
            i >>= 1

        ok = False

        for height in range(1, 8):
            made_bits_len = 2 ** height - 1

            if made_bits_len < len(bits):
                continue

            made_bits = bits + [0] * (made_bits_len - len(bits))
            build_dfs(1, 1, height, made_bits[:])

            if checker_dfs(1, 1, height) == 1:
                ok = True
                break

        ans.append(int(ok))

    return ans
