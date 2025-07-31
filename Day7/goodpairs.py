# def numIdenticalPairs_brute_force_verbose(nums: list[int]) -> int:
#     """
#     Calculates the number of good pairs using a brute-force nested loop approach,
#     with detailed print statements to show execution flow.
#     """
#     count = 0
#     n = len(nums)
#     print(f"\n--- Brute-Force (Verbose) for nums: {nums} ---")
#     print(f"Initial count: {count}")
#     print(f"Array length (n): {n}\n")

#     # Outer loop for index i
#     for i in range(n):
#         print(f"Outer loop: Current i = {i}, nums[i] = {nums[i]}")
#         # Inner loop for index j, starting from i + 1 to ensure i < j
#         for j in range(i + 1, n):
#             print(f"  Inner loop: Current j = {j}, nums[j] = {nums[j]}")
#             if nums[i] == nums[j]:
#                 count += 1
#                 print(f"    Match found! (nums[{i}] == nums[{j}]), {nums[i]} == {nums[j]}")
#                 print(f"    Count incremented to: {count}")
#             else:
#                 print(f"    No match: nums[{i}] ({nums[i]}) != nums[{j}] ({nums[j]})")
#         print(f"Outer loop for i={i} finished. Current total count: {count}\n")

#     print(f"--- Brute-Force (Verbose) finished ---")
#     print(f"Final good pairs count: {count}")
#     return count

# # --- Test Cases with Verbose Output ---
# numIdenticalPairs_brute_force_verbose([1,2,3,1,1,3])
# numIdenticalPairs_brute_force_verbose([1,1,1,1])
# numIdenticalPairs_brute_force_verbose([1,2,3])

# def numIdenticalPairs_hash_map_verbose_revised(nums: list[int]) -> int:
#     """
#     Calculates the number of good pairs using a standard dictionary (hash map)
#     for frequency counting, with detailed print statements to show execution flow.
#     """
#     counts = {} # Using a standard dictionary
#     print(f"\n--- Hash Map (Verbose - Revised) for nums: {nums} ---")
#     print(f"Initial counts map: {counts}")

#     # Step 1: Populating the counts map
#     print("\n--- Step 1: Populating frequency map ---")
#     for num in nums:
#         print(f"  Processing number: {num}")
#         # Check if the number is already in the dictionary
#         if num in counts:
#             counts[num] += 1
#             print(f"    '{num}' already in map. Count incremented to: {counts[num]}")
#         else:
#             counts[num] = 1
#             print(f"    '{num}' not in map. Added with count: {counts[num]}")
#         print(f"    Counts updated: {counts}")
#     print(f"\nFinal frequency map: {counts}")

#     good_pairs_count = 0
#     print(f"Initial good_pairs_count: {good_pairs_count}")

#     # Step 2: Calculate good pairs from frequencies
#     print("\n--- Step 2: Calculating good pairs from frequencies ---")
#     for value, count in counts.items():
#         print(f"  Processing value: {value} with frequency: {count}")
#         if count >= 2:
#             pairs_for_value = (count * (count - 1)) // 2
#             good_pairs_count += pairs_for_value
#             print(f"    Frequency >= 2. Calculating pairs for {value}: ({count} * ({count} - 1)) / 2 = {pairs_for_value}")
#             print(f"    good_pairs_count incremented to: {good_pairs_count}")
#         else:
#             print(f"    Frequency < 2 ({count}), no pairs can be formed from this value.")
    
#     print(f"\n--- Hash Map (Verbose - Revised) finished ---")
#     print(f"Final good pairs count: {good_pairs_count}")
#     return good_pairs_count

# # --- Test Cases with Verbose Output ---
# numIdenticalPairs_hash_map_verbose_revised([1,2,3,1,1,3])
# numIdenticalPairs_hash_map_verbose_revised([1,1,1,1])
# numIdenticalPairs_hash_map_verbose_revised([1,2,3])

# def numIdenticalPairs_array_freq_verbose(nums: list[int]) -> int:
#     """
#     Calculates the number of good pairs using an array as a frequency map,
#     with detailed print statements to show execution flow.
#     """
#     # Create a frequency array. Max value is 100, so size 101 for indices 0-100.
#     # Initialize all counts to 0.
#     freq = [0] * 101
#     print(f"\n--- Array Freq (Verbose) for nums: {nums} ---")
#     print(f"Initial frequency array (first few elements): {freq[:5]} ... {freq[-5:]}")

#     # Step 1: Populate the frequency array
#     print("\n--- Step 1: Populating frequency array ---")
#     for num in nums:
#         print(f"  Processing number: {num}")
#         freq[num] += 1
#         # Print relevant part of freq array for clarity
#         print(f"    freq[{num}] incremented. Current freq[{num}]: {freq[num]}")
#         # To avoid printing the whole array, just show the updated entry or a snippet
#         # print(f"    Current frequency array (snippet): {freq[max(0, num-2):min(101, num+3)]}")
    
#     # Print a more concise representation of the final frequency array
#     final_freq_dict = {i: freq[i] for i in range(1, 101) if freq[i] > 0}
#     print(f"\nFinal populated frequency array (non-zero entries): {final_freq_dict}")


#     good_pairs_count = 0
#     print(f"Initial good_pairs_count: {good_pairs_count}")

#     # Step 2: Calculate good pairs from frequencies
#     print("\n--- Step 2: Calculating good pairs from frequencies ---")
#     # Iterate through the frequency array from index 1 to 100 (inclusive)
#     # The `enumerate` function gives both the index (value) and the element (count)
#     for value, count in enumerate(freq):
#         if value == 0: # Skip index 0 if values are 1-100
#             continue
#         if count > 0: # Only process values that actually appeared
#             print(f"  Processing value: {value} with frequency: {count}")
#             if count >= 2:
#                 pairs_for_value = (count * (count - 1)) // 2
#                 good_pairs_count += pairs_for_value
#                 print(f"    Frequency >= 2. Calculating pairs for {value}: ({count} * ({count} - 1)) / 2 = {pairs_for_value}")
#                 print(f"    good_pairs_count incremented to: {good_pairs_count}")
#             else:
#                 print(f"    Frequency < 2 ({count}), no pairs can be formed from this value.")
    
#     print(f"\n--- Array Freq (Verbose) finished ---")
#     print(f"Final good pairs count: {good_pairs_count}")
#     return good_pairs_count

# # --- Test Cases with Verbose Output ---
# numIdenticalPairs_array_freq_verbose([1,2,3,1,1,3])
# numIdenticalPairs_array_freq_verbose([1,1,1,1])
# numIdenticalPairs_array_freq_verbose([1,2,3])

class Solution:
    def numIdenticalPairs(self, nums) -> int: # Removed List[int] type hint from nums
        """
        Calculates the number of good pairs in the given list of integers,
        using an "on-the-fly" frequency counting method,
        with detailed print statements to show execution flow.
        """
        print(f"\n--- numIdenticalPairs (Your Logic - Verbose) for nums: {nums} ---")

        # This dictionary will store the frequency of each number encountered so far.
        hash_table = {}
        print(f"Initial 'hash_table' dictionary: {hash_table}")

        # This variable will accumulate the count of good pairs.
        good_pairs_count = 0
        print(f"Initial 'good_pairs_count': {good_pairs_count}\n")

        # for every element in nums
        print("--- Iterating through nums ---")
        for i, v in enumerate(nums): # Added enumerate to show current index for clarity in prints
            print(f"  Processing element at index {i}: v = {v}")

            # number of repeated digits (check if 'v' has been seen before)
            if v in hash_table:
                print(f"    '{v}' is already in 'hash_table'. Current count for '{v}': {hash_table[v]}")
                
                # count number of pairs based on duplicate values
                if hash_table[v] == 1:
                    good_pairs_count += 1
                    print(f"    hash_table[{v}] was 1. Added 1 to good_pairs_count.")
                else:
                    good_pairs_count += hash_table[v]
                    print(f"    hash_table[{v}] was {hash_table[v]}. Added {hash_table[v]} to good_pairs_count.")
                
                print(f"    good_pairs_count is now: {good_pairs_count}")
                
                # increment the number of counts for 'v'
                hash_table[v] += 1
                print(f"    Incremented count for '{v}' in 'hash_table'. New count: {hash_table[v]}")
            # number has not been seen before
            else:
                print(f"    '{v}' is not in 'hash_table'. Adding with count of 1.")
                hash_table[v] = 1
            
            print(f"  Current state: hash_table = {hash_table}, good_pairs_count = {good_pairs_count}\n")
        
        # return the total number of good pairs
        print(f"--- Iteration complete ---")
        print(f"Final 'hash_table' dictionary: {hash_table}")
        print(f"Final 'good_pairs_count': {good_pairs_count}")
        return good_pairs_count

# --- Test Cases ---
sol = Solution()

print("--- Running Test Case 1 ---")
result1 = sol.numIdenticalPairs([1,2,3,1,1,3]) # Expected: 4
print(f"Result for [1,2,3,1,1,3]: {result1}\n")

print("--- Running Test Case 2 ---")
result2 = sol.numIdenticalPairs([1,1,1,1])     # Expected: 6
print(f"Result for [1,1,1,1]: {result2}\n")

print("--- Running Test Case 3 ---")
result3 = sol.numIdenticalPairs([1,2,3])       # Expected: 0
print(f"Result for [1,2,3]: {result3}\n")

print("--- Running Test Case 4 ---")
result4 = sol.numIdenticalPairs([7,7,7,7,7])   # Expected: 10
print(f"Result for [7,7,7,7,7]: {result4}\n")