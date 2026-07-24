"""
Problem: Two Sum
Difficulty: Easy

Approach:
- Brute Force
- Nested Loops

Time Complexity: O(n²)
Space Complexity: O(1)
"""
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]