N = int(input())
vote = list(map(int,input().split()))

if vote.count(0) >= (N+1)//2:
	answer = "INVALID"
elif vote.count(1)>vote.count(-1):
	answer = "APPROVED"
else:
	answer = "REJECTED"

print(answer)