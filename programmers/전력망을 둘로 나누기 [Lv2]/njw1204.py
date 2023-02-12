def dfs(i, visited, wires):
    visited[i] = True
    ans = 1

    for wire in wires:
        if i in wire:
            nxt = sum(wire) - i

            if not visited[nxt]:
                visited[nxt] = True
                ans += dfs(nxt, visited, wires)

    return ans

def solution(n, wires):
    ans = 10**9

    for i in range(len(wires)):
        filtered_wires = wires[:i] + wires[i + 1:]
        ans = min(ans, abs(n - 2 * dfs(1, [False]*(n + 1), filtered_wires)))

    return ans