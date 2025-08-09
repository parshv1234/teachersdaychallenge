'''
A. Beautiful Matrix
time limit per test2 seconds
memory limit per test256 megabytes
You've got a 5 × 5 matrix, consisting of 24 zeroes and a single number one. Let's index the matrix rows by numbers from 1 to 5 from top to bottom, let's index the matrix columns by numbers from 1 to 5 from left to right. In one move, you are allowed to apply one of the two following transformations to the matrix:

Swap two neighboring matrix rows, that is, rows with indexes i and i + 1 for some integer i (1 ≤ i < 5).
Swap two neighboring matrix columns, that is, columns with indexes j and j + 1 for some integer j (1 ≤ j < 5).
You think that a matrix looks beautiful, if the single number one of the matrix is located in its middle (in the cell that is on the intersection of the third row and the third column). Count the minimum number of moves needed to make the matrix beautiful.

Input
The input consists of five lines, each line contains five integers: the j-th integer in the i-th line of the input represents the element of the matrix that is located on the intersection of the i-th row and the j-th column. It is guaranteed that the matrix consists of 24 zeroes and a single number one.

Output
Print a single integer — the minimum number of moves needed to make the matrix beautiful.
'''

# matrix = [list(map(int, input().split())) for _ in range(5)]
# one_position = [(i, row.index(1)) for i, row in enumerate(matrix) if 1 in row][0]
# target_position = (2, 2)  
# moves = abs(one_position[0] - target_position[0]) + abs(one_position[1] - target_position[1])
# print(moves)


# Initialize variables to store the position of the '1'
row_one = 0
col_one = 0

# Loop through the 5 rows of the matrix
for i in range(5):
    # Read a row of input and convert it to a list of integers
    row = list(map(int, input().split()))
    
    # Check if '1' is in the current row
    for j in range(5):
        if row[j] == 1:
            # Store the 1-indexed row and column number
            row_one = i + 1
            col_one = j + 1
            # We found the '1', no need to search further
            break
    if row_one != 0:
        break

# The center of the matrix is at (3, 3)
center_row = 3
center_col = 3

# Calculate the number of moves needed for rows and columns separately
row_moves = abs(row_one - center_row)
col_moves = abs(col_one - center_col)

# The total minimum moves is the sum of row and column moves
total_moves = row_moves + col_moves

print(total_moves)