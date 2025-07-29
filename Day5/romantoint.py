class Solution(object):
    def romanToInt(self, s):
        """
        Converts a Roman numeral string to an integer.
        
        :type s: str
        :rtype: int
        """
        # Step 1: My mapping of Roman symbols to their integer values
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # Step 2: Initialize my total sum
        total = 0
        n = len(s) # Storing length for cleaner loop bounds checking

        print(f"\n--- My Dry Run for Input: '{s}' ---")
        print(f"Starting total: {total}")

        # Step 3: Iterate through the Roman numeral string from left to right
        for i in range(n):
            current_symbol = s[i]
            current_value = roman_map[current_symbol]
            
            print(f"\nProcessing Index {i}: Symbol = '{current_symbol}', Value = {current_value}")

            # Step 3.1: Check if it's a subtractive case
            # This happens if there's a next character AND its value is greater than the current one.
            if i + 1 < n and current_value < roman_map[s[i+1]]:
                print(f"  --> Found a subtractive pattern! ({current_value} < {roman_map[s[i+1]]} for '{current_symbol}{s[i+1]}')")
                total -= current_value # Subtract the current value
                print(f"  --> Subtracting {current_value}. Current total: {total}")
            else:
                # Step 3.2: Otherwise (additive case), just add the current value
                print(f"  --> Additive pattern. Adding {current_value}.")
                total += current_value # Add the current value
                print(f"  --> Current total: {total}")
        
        # Step 4: Return my accumulated total
        print(f"\n--- Finished. My Final Calculated Integer: {total} ---")
        return total

# --- My Test Cases ---
if __name__ == "__main__":
    my_solution = Solution()

    print("--- Running My Roman to Integer Tests ---")

    test_cases = [
        ("III", 3),           # Simple additive
        ("LVIII", 58),        # Mix of additive
        ("MCMXCIV", 1994),    # Complex, all subtractive types
        ("IV", 4),            # Simple subtractive (I before V)
        ("IX", 9),            # Simple subtractive (I before X)
        ("XL", 40),           # Simple subtractive (X before L)
        ("XC", 90),           # Simple subtractive (X before C)
        ("CD", 400),          # Simple subtractive (C before D)
        ("CM", 900),          # Simple subtractive (C before M)
        ("MMMCMXCIX", 3999),  # Largest possible
        ("I", 1)              # Smallest possible
    ]

    for roman_str, expected_int in test_cases:
        actual_int = my_solution.romanToInt(roman_str)
        print(f"  Input: '{roman_str}'")
        print(f"  My Result: {actual_int}")
        print(f"  Expected: {expected_int}")
        print(f"  Test Passed: {actual_int == expected_int}\n")