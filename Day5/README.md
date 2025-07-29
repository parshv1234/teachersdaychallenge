# Intuition

The Roman numeral system initially seemed a bit tricky because of 
those "subtraction" rules (like IV for 4 instead of IIII). 
But after looking at the examples, my core intuition is:

1. **Map symbols to values:**  
   Use a dictionary (hash map) for quick lookups of {I, V, X, L, C, D, M}.

2. **Left-to-Right Scan:**  
   Roman numerals are processed from **left to right**.

3. **The "Look Ahead" Rule:**  
   - If the **current value < next value**, it’s a *subtractive case* → **subtract**.  
   - Otherwise (≥ next value or last character), it’s an *additive case* → **add**.  

4. By following this "look ahead and decide to **add** or **subtract**" logic, 
   we arrive at the correct total.

# Approach

1. **Define a dict:**  
   Create a dictionary for Roman numeral values (O(1) lookup).

2. **Initialize Total:**  
   Start with `total = 0`.

3. **Iterate and Apply Logic:**  
   For each index `i` in the string:
   - Get the current symbol’s value.
   - If `i+1 < len(s)` and current_value < next_value → **subtract**.  
   - Otherwise → **add**.

4. **Return Total:**  
   At the end, `total` is the integer equivalent.


# Complexity

* **Time Complexity:**  $$O(n)$$  
  Each symbol is processed once.

* **Space Complexity:**  $$O(1)$$
  Dictionary has 7 fixed entries.  
  No additional structures that grow with input size.


# Dry Run Example

Let’s test with: `s = "MCMXCIV"`

```text
dict = {'I':1, 'V':5, 'X':10, 'L':50, 
             'C':100, 'D':500, 'M':1000}

total = 0  
n = 7  

Index | Symbol | Value | Next Symbol | Next Value | Action    | Total
------+--------+-------+-------------+------------+---------------+---
  0   |   M    | 1000  |     C       |    100     | Add       | 1000
  1   |   C    | 100   |     M       |   1000     | Subtract  | 900
  2   |   M    | 1000  |     X       |     10     | Add       | 1900
  3   |   X    | 10    |     C       |    100     | Subtract  | 1890
  4   |   C    | 100   |     I       |     1      | Add       | 1990
  5   |   I    | 1     |     V       |     5      | Subtract  | 1989
  6   |   V    | 5     |     -       |     -      | Add       | 1994

✅ Final Result: 1994
```

# Code
```python []
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        total = 0
        n = len(s) 
        for i in range(n):
            current_value = dict[s[i]]
            if i + 1 < n and current_value < dict[s[i+1]]:
                total -= current_value
            else:
                total += current_value
        return total
        
```