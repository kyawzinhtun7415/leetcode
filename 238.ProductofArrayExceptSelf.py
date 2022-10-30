from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        list = []
        for i in range(len(nums)):
            prefix = nums[i]
            postfix = nums[i ]