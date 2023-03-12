n,m=map(int,input().split())
d=10**9+7
x=2**n-1
print([x,x%d*m*2-1][m>1]%d)
