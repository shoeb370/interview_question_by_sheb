"""

Given an array of numbers `nums` and an integer `target`, return indices of any two numbers from the list such that they add up to `target`.

You may assume the input will have exactly one solution, and you cannot use the same element twice.

Example: nums = [2, 7, 11, 15], target = 9

Return: [0, 1]

"""
def two_sum(nums, target):
    # Initialize an empty dictionary to store indices of elements
    index_map = {}
    
    # Iterate through the list of numbers
    for i, num in enumerate(nums):
        # Calculate the complement
        complement = target - num
        
        # Check if the complement exists in the dictionary
        if complement in index_map:
            # If it does, return the indices of the current number and the complement
            return [index_map[complement], i]
        
        # Otherwise, add the current number and its index to the dictionary
        index_map[num] = i

# Example usage:
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1]
