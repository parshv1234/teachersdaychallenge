def twoSum(nums, target):
    """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
    """
    num_map = {}  

    for i, num in enumerate(nums):
        complement = target - num
        print(f"Index: {i}, Number: {num}, Complement: {complement}, Map: {num_map}")
        if complement in num_map:
            print(f"Found: {num} + {complement} = {target}")
            print(f"Returning indices: {num_map[complement]} and {i}")
            return [num_map[complement], i]
            
        num_map[num] = i
        print(f"Added {num} to map with index {i}")
        print(f"Updated Map: {num_map}")

    return []

print(twoSum([3,3],6))