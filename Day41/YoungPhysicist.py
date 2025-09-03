n = int(input())
resA = 0
resB = 0
resC = 0

for _ in range(n):
    a, b, c = map(int, input().split())
    resA += a
    resB += b
    resC += c

if resA == 0 and resB == 0 and resC == 0:
    print("YES")
else:
    print("NO")

