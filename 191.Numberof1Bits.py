# solution1 which counts all bits
# runtime = O(32) 
# due to binary string of length (32) specified by problem

# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         res = 0
#         # n != 0 or n > 0
#         while n:
#             res += n % 2
#             n = n >> 1
#         return res

# solution2 which counts only bits which are 1
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        # n != 0 or n > 0
        while n:
            n &= n - 1
            res += 1
        return res

n = [0b00000000000000000000000000001011,
        0b11111111111111111111111111111101,
        0b00000000000000000000000010000000]
for i in n:
    sol = Solution().hammingWeight(i)
    print(sol)