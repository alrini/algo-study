t,k = map(int, input().split())
league = [[0]*4 for _ in range(4)]

for i in range(4):
    for j, score in enumerate(map(int, input().split())):
        league[i][j] = score

left = 0
right = 10**12

while left<right:
    mid = (left+right)//2
    
