n = int(input())
f_n = 0
# for i in range(1, n + 1):
#     f_n += ((-1)**i) * i

if n % 2 == 0:
    f_n = n // 2
else:
    f_n = -(n + 1) // 2


print(f_n)