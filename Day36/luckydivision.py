n = int(input())

lucky_numbers = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]

is_almost_lucky = False

for lucky_num in lucky_numbers:
    if n % lucky_num == 0:
        is_almost_lucky = True
        break

if is_almost_lucky:
    print("YES")
else:
    print("NO")


# n = int(input())

# lucky_digits = {'4','7'}
# if all(digit in lucky_digits for digit in str(n)):
#     print("YES")
# elif n % 4 == 0 or n % 7 == 0:
#     print("YES")
# else:
#     print("NO")