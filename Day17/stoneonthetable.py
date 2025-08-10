'''
A. Stones on the Table
time limit per test2 seconds
memory limit per test256 megabytes
There are n stones on the table in a row, each of them can be red, green or blue. Count the minimum number of stones to take from the table so that any two neighboring stones had different colors. Stones in a row are considered neighboring if there are no other stones between them.

Input
The first line contains integer n (1 ≤ n ≤ 50) — the number of stones on the table.

The next line contains string s, which represents the colors of the stones. We'll consider the stones in the row numbered from 1 to n from left to right. Then the i-th character s equals "R", if the i-th stone is red, "G", if it's green and "B", if it's blue.

Output
Print a single integer — the answer to the problem.
'''

n = int(input())
s = input()
count = 0
for i in range(1,n):
    if s[i] == s[i-1]:
        count += 1

print(count)

# n = int(input())
# s = input()
# stack = []
# removals = 0
# for stone in s:
#     if stack and stack[-1] == stone:
#         removals += 1
#     else:
#         stack.append(stone)
# print(removals)