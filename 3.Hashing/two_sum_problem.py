#Problem Statement:
#Given a list of integers a and a target integer target, return the indices of the two numbers such that they add up to the target.
#Assume that exactly one solution exists and you may not use the same element twice.

from typing import List  # typing module se List import karo

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}  # value : index

        for i, num in enumerate(nums):
            diff = target - num
            if diff in num_map:
                return [num_map[diff], i]
            num_map[num] = i

        return []  # If no pair found
sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))