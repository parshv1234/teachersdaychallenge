T = int(input())
chars = []
group = 1
for _ in range(T):
    chars.append(input())
# print(chars)
for i in range(1, T):
    # print(f"At i:{i}")
    # print(chars[i],chars[i-1])
    if chars[i] != chars[i-1]:
        group += 1
print(group)
    # elif :
    #     group += 1
    #     print(group)
    # else:
    #     continue
# if '00' or '11'in magnets:
#     count += 1
#     print(count)


##########################    optimized code    ###############################

# Read the number of magnets
n = int(input())

# If there are no magnets, there are no groups.
if n == 0:
    print(0)
else:
    # The first magnet always starts the first group.
    groups = 1

    # Read the first magnet to compare against.
    previous_magnet = input()

    # Loop for the rest of the n-1 magnets.
    for _ in range(n - 1):
        current_magnet = input()
        
        # If the current magnet is different, it forms a new group.
        if current_magnet != previous_magnet:
            groups += 1
        
        # The current magnet now becomes the 'previous' one for the next loop.
        previous_magnet = current_magnet

    print(groups)