from typing import List

# my solution
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         set1 = set()
#         for i in nums:
#             if i not in set1:
#                 set1.add;
#             else:
#                 return True
#         return False


# pythonic solution
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

# nums = [1,2,3,1]
nums = [1,2,3,4]
sol = Solution().containsDuplicate(nums)
print(sol)