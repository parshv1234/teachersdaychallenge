n = int(input())
allpoints = list(map(int, input().split()))
amazing_count = 0

best = allpoints[0]
worst = allpoints[0]

for i in range(1, len(allpoints)):
    if allpoints[i] < worst:
        worst = allpoints[i]
        # print(worst)
        amazing_count += 1
    if allpoints[i] > best:
        best = allpoints[i]
        # print(best)
        amazing_count += 1
print(amazing_count)