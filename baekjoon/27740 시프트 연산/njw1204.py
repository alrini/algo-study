n = int(input())
a = [(i + 1) for i, val in enumerate(map(int, input().split())) if val == 1]
ans = min(
  {"T": 1, "L": a[-1], "R": 0},
  {"T": 2, "L": 0, "R": (n + 1 - a[0])},
  key=lambda x: x["L"] + x["R"]
)

for i in range(len(a) - 1):
  left, right = a[i], a[i + 1]
  ans = min(
    ans,
    {"T": 1, "L": left, "R": (left + n + 1 - right)},
    {"T": 2, "L": (left + n + 1 - right), "R": (n + 1 - right)},
    key=lambda x: x["L"] + x["R"]
  )

print(ans["L"] + ans["R"])

if ans["T"] == 1:
  print("L" * ans["L"] + "R" * ans["R"])
else:
  print("R" * ans["R"] + "L" * ans["L"])
