n = int(input())
x = [*map(int,input().split())]

if x.count(0) >= (n + 1) // 2:
    print("INVALID")
elif x.count(1) > x.count(-1):
    print("APPROVED")
else:
    print("REJECTED")
