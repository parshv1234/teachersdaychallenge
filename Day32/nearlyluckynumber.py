n = input()

lucky_digit_count = 0

for digit in n:
    if digit == '4' or digit == '7':
        lucky_digit_count += 1

if lucky_digit_count == 4 or lucky_digit_count == 7:
    print("YES")
else:
    print("NO")
    
# for values in num_map.values():
#     if values in n:
#         count += 1
# print(count)