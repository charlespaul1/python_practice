# given an array of integers and an integer target, return indices of the two numbers such that they add up to target
nums = [2, 7, 11, 15]
target = 9
def two_sum(nums, target):
# dictionary to store indices of the number
    num_indices = {}
# iterate thru the array
    for i, num in enumerate(nums):
    # check if compiment (target - num) exists in the dictionary
        complement = target - num
        if complement in num_indices:
            return [num_indices[complement], i]
        num_indices[num] = i
    return []

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))