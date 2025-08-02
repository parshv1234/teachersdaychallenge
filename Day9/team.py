n = int(input())
problems_to_solve = 0

for _ in range(n):
    opinions = list(map(int, input().split()))
    
    if sum(opinions) >= 2:
        problems_to_solve += 1

print(problems_to_solve)