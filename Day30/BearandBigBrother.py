limak_weight, bob_weight = map(int, input().split())
years = 0
while limak_weight <= bob_weight:
    limak_weight *= 3
    bob_weight *= 2
    
    years += 1
print(years)
