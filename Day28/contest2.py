t = int(input())
for _ in range(t):
    n = int(input())
    result = []
    power_of_10 = 10
    while (1 + power_of_10) <= n:
        # print(k)
        d = (1 + power_of_10)
        # print(d)
        if n % d == 0:
            x = n // d
            if x % 10 != 0:
                result.append(x)
        power_of_10 *= 10
    if not result:
        print(0)
    else:
        result.sort()
        print(len(result))
        print(*result)