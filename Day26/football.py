s = input()

n = len(s)

is_dangerous = False

if n < 7:
    is_dangerous = False
else:
    for i in range(n - 6):
        if s[i:i+7] == "0000000" or s[i:i+7] == "1111111":
            is_dangerous = True
            break

if is_dangerous:
    print("YES")
else:
    print("NO")