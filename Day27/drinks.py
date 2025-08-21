n = int(input())
percent = list(map(int, input().split()))

total_percent = sum(percent)
final_conc = total_percent/n
print(final_conc)
    