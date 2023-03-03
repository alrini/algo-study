def solution(numbers):
    ans = []

    for number in numbers:
        least_ones = 0
        i = number

        while i & 1:
            least_ones += 1
            i >>= 1

        if least_ones > 0:
            ans.append(number - (1 << (least_ones - 1)) + (1 << least_ones))
        else:
            ans.append(number + 1)

    return ans
