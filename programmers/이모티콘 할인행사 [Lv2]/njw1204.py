def solution(users, emoticons):
    ans = [-1, -1]

    for case in range(4 ** len(emoticons)):
        sales = []
        joined = 0
        purchased = 0

        for emoticon in emoticons:
            discount = 10 + (case % 4 * 10)
            sales.append([emoticon * (100 - discount) // 100, discount])
            case //= 4

        for user in users:
            amount = sum([sale[0] for sale in sales if sale[1] >= user[0]])

            if amount >= user[1]:
                joined += 1
            else:
                purchased += amount

        ans = max(ans, [joined, purchased])

    return ans