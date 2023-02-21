def solution(name):
    for move in range(len(name)):
        for move_first in range(move + 1):
            for op in ["L" * move_first + "R" * (move - move_first), "R" * move_first + "L" * (move - move_first)]:
                idx = 0
                temp = list(name)
                temp[idx] = "A"

                for o in op:
                    if o == "L":
                        idx = (idx - 1) % len(temp)
                    else:
                        idx = (idx + 1) % len(temp)

                    temp[idx] = "A"

                if all(i == "A" for i in temp):
                    edit = 0

                    for i in name:
                        edit += min(ord(i) - ord("A"), ord("Z") + 1 - ord(i))

                    return move + edit