class Solution:
    def isValid(self, s: str) -> bool:
        """
        Determines if the input string 's' contains valid parentheses.
        Valid parentheses follow two rules:
        1. Open brackets must be closed by the same type of brackets.
        2. Open brackets must be closed in the correct order.
        
        :type s: str
        :rtype: bool
        """
        # My stack to keep track of opening brackets
        stack = []
        
        # My mapping for closing brackets to their corresponding opening brackets
        mapping = {
            ")": "(",
            "}": "{",
            "]": "["
        } 

        print(f"\n--- Validating String: '{s}' ---")
        print(f"Initial Stack: {stack}")

        # Iterate through each character in the input string
        for i, char in enumerate(s):
            print(f"\nProcessing char '{char}' at index {i}:")

            # If the character is an opening bracket (one of the values in my mapping)
            if char in mapping.values():
                print(f"  '{char}' is an opening bracket. Pushing onto stack.")
                stack.append(char)
                print(f"  Stack after push: {stack}")
            # If the character is a closing bracket (one of the keys in my mapping)
            elif char in mapping.keys():
                print(f"  '{char}' is a closing bracket.")
                
                # Check if the stack is empty BEFORE trying to pop
                if not stack:
                    print(f"  Error: Stack is empty, but found closing bracket '{char}'. Invalid.")
                    return False # Found closing bracket with no corresponding opening bracket
                
                # Pop the top element from the stack
                top_element = stack.pop()
                print(f"  Popped '{top_element}' from stack. Stack now: {stack}")
                
                # Check if the popped element matches the expected opening bracket for the current closing bracket
                expected_open_bracket = mapping[char]
                if top_element != expected_open_bracket:
                    print(f"  Error: Mismatch! Expected '{expected_open_bracket}' but got '{top_element}'. Invalid.")
                    return False # Mismatch between opening and closing brackets
                else:
                    print(f"  Match found! '{top_element}' paired with '{char}'.")
            
            # If the character is not a bracket (problem constraints usually guarantee only brackets,
            # but this is good practice if other chars were allowed)
            # else:
            #     # You could handle other characters here, perhaps skipping them or returning False
            #     pass 
        
        # After iterating through all characters, check if the stack is empty.
        # If it's empty, all opening brackets were correctly closed.
        # If it's not empty, some opening brackets were never closed.
        print(f"\n--- Finished processing. Final Stack: {stack} ---")
        if not stack:
            print("  Stack is empty. All brackets matched. Result: True")
            return True
        else:
            print("  Stack is NOT empty. Some brackets were unclosed. Result: False")
            return False

# --- My Test Cases ---
if __name__ == "__main__":
    my_solution = Solution()

    print("--- Running My Valid Parentheses Tests ---")

    test_cases = [
        ("()", True),            # Simple valid
        ("()[]{}", True),        # Multiple types, valid
        ("{[]}", True),          # Nested valid
        ("([{}])", True),        # Deeply nested valid
        ("(]", False),           # Mismatch type
        ("([)]", False),         # Mismatch order
        ("{", False),            # Unclosed open bracket
        ("}", False),            # Unopened close bracket
        ("", True),              # Empty string (usually considered valid)
        ("((", False),           # Multiple unclosed open
        ("))", False),           # Multiple unopened close
    ]

    for s_input, expected_output in test_cases:
        actual_output = my_solution.isValid(s_input)
        print(f"  Input: '{s_input}'")
        print(f"  My Result: {actual_output}")
        print(f"  Expected: {expected_output}")
        print(f"  Test Passed: {actual_output == expected_output}\n")