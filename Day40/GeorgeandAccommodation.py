n = int(input())
count = 0

for _ in range(n):
    p, q = input().split()
    # print(f"P is:{p}, Q is: {q}")
    p = int(p)
    q = int(q)
    if q - p >= 2:
        count += 1
print(count)