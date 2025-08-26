num1 = input()
num2 = input()
ans = ""
for i in range(len(num1)):
    # print(f"The i-th digit of num1 is:{num1[i]} and num2 is: {num2[i]}")
    if num1[i] != num2[i]:
        ans += '1'
    else:
        ans += '0'
print(ans)