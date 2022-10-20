# def pivotIndex(nums):
#     i = 0
#     while i < len(nums):
#         sum_left = nums[:i]
#         print("sum_left", sum_left)
#         sum_right = nums[i + 1:]
#         print("sum_right", sum_right)
#         left_sum = sum(sum_left)
#         right_sum = sum(sum_right)
#         print("left_sum", left_sum)
#         print("right_sum", right_sum)
#         if left_sum == right_sum:
#             return i
#         i += 1
#     return -1


# # leetcode correct solution
# def pivotIndex(nums):
#     left, right = 0, sum(nums)
#     for index, num in enumerate(nums):
#         right -= num
#         if left == right:
#             return index
#         left += num
#     return -1

# neetcode correct solution
def pivotIndex(nums):
    total = sum(nums)
    left = 0
    for i in range(len(nums)):
        right = total - left - nums[i]
        if left == right:
            return i
        left += nums[i]
    return -1 

# test case
list1 = [1,7,3,6,5,6]
list2 = [1,2,3]
list3 = [2,1,-1]
print(pivotIndex(list1))
print(pivotIndex(list2))
print(pivotIndex(list3))
        