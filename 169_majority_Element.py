# from black import List


# def majorityElement(nums: List[int]) -> int:
#     # turn it into a dictionary
#     counts = dict()
#     for i in nums:
#         counts[i] = counts.get(i, 0) + 1 # if no key, give 0 as a value
    
#     # return the key and the max is according to the value
#     return max(counts, key=counts.get) 

# print(majorityElement([2,2,1,1,1,2,2]))


def majorityElement(nums):
    majority_count = len(nums)//2
    print(majority_count)
    for num in nums:
        count = sum(1 for elem in nums if elem == num)
        print(count)
        if count > majority_count:
            return num

print(majorityElement([2,2,1,1,1,2,2]))