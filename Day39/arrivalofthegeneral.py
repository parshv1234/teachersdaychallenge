n = int(input())
lineup = list(map(int, input().split()))
max_height = max(lineup)
min_height = min(lineup)

max_index = 0
for i in range(n):
    if lineup[i] == max_height:
        max_index = i
        break

min_index = 0
for i in range(n - 1, -1, -1):
    if lineup[i] == min_height:
        min_index = i
        break

swaps_for_max = max_index
swaps_for_min = (n - 1) - min_index
total_swaps = swaps_for_max + swaps_for_min

if max_index > min_index:
    total_swaps -= 1

print(total_swaps)