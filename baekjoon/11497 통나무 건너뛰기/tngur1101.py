t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    result = 0
    for j in range(2,n):
        diff = arr[j] - arr[j-2]
        result = max(diff, result)

    print(result)