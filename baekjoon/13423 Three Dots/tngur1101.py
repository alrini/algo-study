t = int(input())

def binary_search(left, right, t):
    while left<=right:
        mid = (left+right)//2
        if dots[mid]==t:
            return 1
        elif dots[mid] > t:
            right = mid-1
        else:
            left = mid+1
    return 0

for _ in range(t):
    n = int(input())
    answer = 0
    dots = list(map(int, input().split()))
    dots.sort()
    left, right = 0, n-1

    for i in range(n-1):
        for j in range(i+1, n):
            dist = abs(dots[j]-dots[i])
            if binary_search(left, right, dots[j]+dist):
                answer +=1


    print(answer)

