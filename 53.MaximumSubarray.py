from black import List
"""
runtime = 0(n)
"""

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         max_sub = nums[0]
#         cur_sum = 0

#         for n in nums:
#             if cur_sum < 0:
#                 cur_sum = 0
#             cur_sum += n
#             max_sub = max(max_sub, cur_sum)
#         return max_sub


# Kadane's Algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_cur = max_global = nums[0]

        for n in nums[1:]:
            max_cur = max(n, max_cur + n)
            if max_cur > max_global:
                max_global = max_cur
        
        return max_global



sol1 = Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
sol2 = Solution().maxSubArray([5,4,-1,7,8])
print(sol1)
print(sol2) 