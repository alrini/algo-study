def cmp(t, a, i, x):
	global n, k

	if t == 0:
		is_allow = (i - 1 < 0 or x > a[i - 1]);
		return (not is_allow, x)
	else:
		is_allow = (i + k > n - 1 or x < a[i + k]);
		return (is_allow, x)

n, k = map(int, input().split())
a = [*map(int, input().split())]
ans = 0

for i in range(n - k + 1):
	ta = a[:]

	for t in range(2):
		ta[i:i+k] = sorted(ta[i:i+k], key=lambda x: cmp(t, ta, i, x))
		tans = 0

		for j in range(n):
			if j == 0 or ta[j] > ta[j - 1]:
				tans += 1
				ans = max(ans, tans)
			else:
				tans = 1

print(ans)
