n = int(input())
size = list(map(int, input().split()))
# print(size)
result = []
# i = 1
max_water = 0
# left = size[i-1]
# right = size[i+1]
if n == 0:
    print(0)
else:
    for idx in range(n):
        max_water = 1
        # print(f"ith term {idx}, num: {size[idx]}")
        # print(f"left={left}")
        for i in range(idx - 1, -1, -1):
            # print(f"left={size[i-1]}")
            if size[i] <= size[i + 1]:
                max_water += 1
            else:
                break
        for i in range(idx + 1, n):
            if size[i] <= size[i - 1]:
                max_water += 1
            else:
                break

        result.append(max_water)
    print(max(result))
        
