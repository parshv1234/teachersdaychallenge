s = input()

upper_count = 0
lower_count = 0

for letter in s:
    if letter.isupper():
        upper_count += 1
    else:
        lower_count += 1
if upper_count <= lower_count:
    print(s.lower())
else:
    print(s.upper())


# l = s.lower()
# u = s.upper()
# # lst1 = list(s)
# # lst2 = list(l)
# # lst3 = list(u)

# diff_manual = [item for item in list(s) if item not in list(l)]
# diff_manual2 = [item for item in list(s) if item not in list(u)]
# if diff_manual <= diff_manual2:
#     print(l)
# else:
#     print(u)


# # # for letter in s:
# #     # lst.append(letter)
# # a =len(lst1 - lst2)
# # b =len(lst1 - lst3)
# # if a <= b:
# #     print(l)
# # else:
# #     print(u)

# # print(lst1.intersection(lst2))
#     # if len(s.lower()) >= len(s.upper()):
#     #     print(s.lower())
#     # else:# len(letter.lower()) < len(letter.upper()):
#     #     print(s.upper())

        