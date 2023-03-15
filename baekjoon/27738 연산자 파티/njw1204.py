n=int(input())
a,b,c,d,e,f=map(int,input().split())
s=max(1,n//f*f+1)
x=0

for i in range(s,n+1):
  if i%a==0: x+=i
  if i%b==0: x%=i
  if i%c==0: x&=i
  if i%d==0: x^=i
  if i%e==0: x|=i
  if i%f==0: x>>=i

print(x)
