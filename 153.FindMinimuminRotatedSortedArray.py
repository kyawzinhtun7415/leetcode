from black import List
# binary search

class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l = 0
        r = len(nums) - 1

        # binary search 
        while l <= r:
            # Since it is a normal sorted array and not a rotated array anymore
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            # do not use len(nums), the array is constantly shrinking binarily
            m = (l + r) // 2
            res = min(res, nums[m])
            # middle > left, search right
            if nums[m] >= nums[l]:
                l = m + 1
            # middle < left/ middle > right, search left
            else:
                r = m - 1
        
        return res

sol = Solution()
print(sol.findMin([3,4,5,1,2]))
print(sol.findMin([4,5,6,7,0,1,2]))
print(sol.findMin([11,13,15,17]))
print(sol.findMin([2,1]))


