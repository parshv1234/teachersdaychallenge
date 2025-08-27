n = int(input())
gifts_received = list(map(int, input().split()))
gifts_givenby = [0] * n

for i in range(n):
    giver = i + 1
    receiver = gifts_received[i]
    
    gifts_givenby[receiver - 1] = giver

print(" ".join(map(str, gifts_givenby)))