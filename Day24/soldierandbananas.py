k, n, w = map(int, input().split())

borrow = 0

for i in range(1, w + 1):
    cost = i * k
    if n  >= 0:
        n -= cost
        if n < 0:
            borrow -= n
    else:
        borrow += cost
print(borrow)