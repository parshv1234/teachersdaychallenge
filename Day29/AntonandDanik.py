# n = int(input())
# games = list(map(str, input()))
# count_a = 0
# count_d = 0
# for win in games:
#     if 'A' == win:
#         count_a += 1
#     else:
#         count_d += 1
# if count_a > count_d:
#     print("Anton")
# elif count_a < count_d:
#     print("Danik")
# else:
#     print("Friendship")

#  or

# n = int(input())
# games = list(map(str, input()))

# count_a = games.count('A')
# count_d = games.count('D')

# if count_a > count_d:
#     print("Anton")
# elif count_a < count_d:
#     print("Danik")
# else:
#     print("Friendship")

#     or  for best time complexity use this......    Basically used a string here instead of list......
n = int(input())
games = input()
 
count_a = games.count('A')
count_d = games.count('D')
 
if count_a > count_d:
    print("Anton")
elif count_a < count_d:
    print("Danik")
else:
    print("Friendship")