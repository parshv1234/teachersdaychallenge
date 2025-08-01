class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        """Generates Pascal's Triangle up to the specified number of rows.
        Each row is a list of integers, and the triangle is represented as a list of lists.
        """        
        print(f"Generating Pascal's Triangle with {numRows} rows.")
        triangle = []
        for i in range(numRows):
            print(f"Generating row {i + 1}")
            row = [1] * (i + 1)
            print(f"Initial row with all 1s: {row}")
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
                print(f"Updated row at index {j}: {row}")
            triangle.append(row)
            print(f"Completed row {i + 1}: {row}")
        print(f"Generated Pascal's Triangle: {triangle}")
        return triangle
# Example usage:
sol = Solution()  

# --- Test Cases ---
print(sol.generate(5))  # Should generate the first 5 rows of Pascal's Triangle
