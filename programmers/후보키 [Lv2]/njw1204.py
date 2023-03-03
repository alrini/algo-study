def solution(relation):
    column_size = len(relation[0])
    ans = []

    for index_size in range(1, column_size + 1):
        for case in range(1, 2 ** column_size):
            keys = []

            for i in range(column_size):
                if case & 1:
                    keys.append(i)

                case >>= 1

            if len(keys) != index_size:
                continue

            if len(set([tuple([row[key] for key in keys]) for row in relation])) != len(relation):
                continue

            if any(all(i in keys for i in prev_ans) for prev_ans in ans):
                continue

            ans.append(keys)

    return len(ans)
