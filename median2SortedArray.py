
def findMedianSortedArrays(nums1, nums2) -> float:
    nums3 = nums1 + nums2
    nums3.sort()
    # print(nums3)
    length = len(nums3)
    # print(length)
    if length % 2 == 0:
        # print(nums3[(length // 2) - 1], nums3[length // 2])
        return (nums3[(length // 2) - 1] + nums3[length // 2])/ 2
    else:
        return nums3[length // 2]

print(findMedianSortedArrays([1,3,5],[2,4,6]))

