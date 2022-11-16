from typing import List

# My inefficient solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        ls = []
        for i in range(length):
            for j in range(length):
                if nums[i] + nums[j] == target and i != j:
                    ls.append(i)
                    ls.append(j)
                    return ls
            