# Intuition

When I look at a string like "{[()]}", my mind immediately thinks about matching pairs.  
An opening parenthesis means I'm starting a "block" that needs to be closed later, while a closing parenthesis needs to match the most recently opened, unclosed one.

This "most recently opened" concept is a perfect fit for a "Last-In, First-Out" (LIFO) data structure, which is exactly what a **stack** is.

My core idea is:
* When I see an **opening bracket**, I'll push it onto a stack to remember it.
* When I see a **closing bracket**, I'll check if the top of the stack has its corresponding opening bracket. If it does, they match ✅ and I pop the opener off the stack.
* After checking all characters, if the **stack is empty**, every bracket found its match. If not, some were left unmatched ❌.


# Approach

1. **Initialize a Stack:**  
   I'll use an empty list in Python to serve as my stack.

2. **Define a Mapping:**  
   A dictionary mapping closing brackets to their corresponding opening brackets 
   (e.g., `")": "("`) provides an easy way to check for valid pairs.

3. **Iterate Through the String:**  
   I'll loop through each character (`char`) in the input string `s`.
   * **If `char` is an opening bracket:** push it onto the stack.
   * **If `char` is a closing bracket:**
       * If the stack is empty → ❌ invalid → return `False`.
       * Otherwise, pop the top element. If it doesn’t match the expected opening bracket → ❌ return `False`.

4. **Final Check:**  
   After the loop, if the stack is empty → ✅ valid string → return `True`.  
   Otherwise → ❌ return `False`.


# Dry Run of Examples

**Example 1: `s = "()[]{}"`**

* `stack = []`, `mapping = {")":"(", "}":"{", "]":"["}`

| Char | Action                                                                  | Stack State |
|:----:|:------------------------------------------------------------------------|:-----------:|
| `(`  | Push `(`                                                                | `['(']`    |
| `)`  | Pop `(`. `'(' == mapping[')']`. ✅ **Match!**                           | `[]`       |
| `[`  | Push `[`                                                                | `['[']`    |
| `]`  | Pop `[`. `'[' == mapping[']']`. ✅ **Match!**                           | `[]`       |
| `{`  | Push `{`                                                                | `['{']`    |
| `}`  | Pop `{`. `'{' == mapping['}']`. ✅ **Match!**                           | `[]`       |

✅ End of loop. Stack empty → **Return `True`**

---

**Example 2: `s = "([)]"`**

* `stack = []`, `mapping = {")":"(", "}":"{", "]":"["}`

| Char | Action                                                                  | Stack State |
|:----:|:------------------------------------------------------------------------|:-----------:|
| `(`  | Push `(`                                                                | `['(']`    |
| `[`  | Push `[`                                                                | `['(', '[']`|
| `)`  | Pop `[`. `'[' != mapping[')']`. ❌ **Mismatch!**                        | `['(']`    |

❌ Mismatch found → **Return `False`**

# Complexity Analysis

- **Time Complexity: O(N)**
  - We iterate through the string of length **N** exactly once.  
  - Each operation (`append`, `pop`, dictionary lookup) is **O(1)**.  
  - ✅ Total → **O(N)**  

- **Space Complexity: O(N)**
  - In the **worst case**, all characters are opening brackets (e.g., `"((((...("`), so the stack holds ~N elements.  
  - ❌ Not constant because stack usage grows with input size.  
  - ✅ Total → **O(N)**  

# Complexity Analysis

| Case        | Time Complexity | Space Complexity | Reason                                                                 |
|-------------|----------------|------------------|------------------------------------------------------------------------|
| Best Case   | O(N)           | O(1)             | String alternates or quickly invalidates → stack never grows much       |
| Worst Case  | O(N)           | O(N)             | All characters are opening brackets before any closing bracket appears |

# Code
```python3 []
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash_map = {")":"(", "}":"{", "]":"["} 

        for char in s:
            if char in hash_map.values():
                stack.append(char)
            elif char in hash_map.keys():
                if not stack or hash_map[char] != stack.pop():
                    return False
        return not stack
```