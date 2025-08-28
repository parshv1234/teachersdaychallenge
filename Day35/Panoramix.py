n, m = map(int, input().split())
nextNum = n + 1

while True:
    is_nextNum_prime = True
    if nextNum <= 1:
        is_nextNum_prime = False
    else:
        for i in range(2, nextNum):
            if nextNum % i == 0:
                is_nextNum_prime = False
                break
    if is_nextNum_prime:
        break
    else:
        nextNum += 1

if nextNum == m:
    print("YES")
else:
    print("NO")


    ################## CORE LOGIC OF PRIME ##################
    # is_nextNum_prime = True
    # if nextNum <= 1:
    #     is_nextNum_prime = False
    # else:
    #     for i in range(2, nextNum):
    #         if nextNum % i == 0:
    #             is_nextNum_prime = False
    #             break
