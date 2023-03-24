t = int(input())

# 서류 점수 순으로 sort하고 두번째를 람다를 이용해서 면접 순으로 sort해서 비교?
for _ in range(t):
    n = int(input())

    answer = 1
    arr = []

    for _ in range(n):
        doc, view = map(int, input().split())
        arr.append((doc, view))

    arr.sort(key=lambda x: x[1])
    #print(arr)
    min_rank = arr[0][0]
    #print(min_rank)

    for i in range(1,n):
        if arr[i][0]<min_rank:
            min_rank = arr[i][0]
            answer+=1

    print(answer)