N = int(input())
A,B,C,D,E,F = map(int, input().split())

X = 0
for i in range(1,N+1):
    if i%A == 0:
        X += i
    if i%B == 0:
        X %= i
    if i%C == 0:
        X &= i
    if i%D == 0:
        X ^= i
    if i%E == 0:
        X |= i
    if i%F == 0:
        X >>= i

answer = X
print(answer)