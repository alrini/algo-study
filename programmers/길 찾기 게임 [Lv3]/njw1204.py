import sys
sys.setrecursionlimit(10 ** 6)

def dfs(node, min_x, max_x, in_nodes_of_height, out_preorder, out_postorder):
    cur_x = node[0][1]
    cur_no = node[1]
    next_height = node[0][0] - 1

    out_preorder.append(cur_no)

    while next_height >= 0 and in_nodes_of_height[next_height]:
        next_node = in_nodes_of_height[next_height][-1]
        next_x = next_node[0][1]
        next_no = next_node[1]

        if min_x <= next_x <= max_x:
            in_nodes_of_height[next_height].pop()

            if next_x < cur_x:
                dfs(next_node, min_x, cur_x - 1, in_nodes_of_height, out_preorder, out_postorder)
            else:
                dfs(next_node, cur_x + 1, max_x, in_nodes_of_height, out_preorder, out_postorder)
        else:
            break

    out_postorder.append(cur_no)

def solution(nodeinfo):
    y_comp = {i: n for n, i in enumerate(sorted(set([i[1] for i in nodeinfo])))}

    nodes_of_heights = {i: list() for i in range(1005)}
    max_height = -1
    root_node = -1

    for node in sorted([((y_comp[i[1]], i[0]), n + 1) for n, i in enumerate(nodeinfo)], reverse=True):
        nodes_of_heights[node[0][0]].append(node)

        if node[0][0] > max_height:
            max_height = node[0][0]
            root_node = node

    ans = [[], []]
    dfs(root_node, -1, 10 ** 9, nodes_of_heights, ans[0], ans[1])
    return ans