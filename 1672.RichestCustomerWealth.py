from black import List


# class Solution:
#     def maximumWealth(self, accounts: List[List[int]]) -> int:
#         customer = []
#         for i in accounts:
#             customer.append(sum(i))
#         return max(customer)

# leetcode solution
class Solution:
    def maximumWealth(self, accounts):
        return max(map(sum, accounts))

solution = Solution()

print(solution.maximumWealth(accounts=[[1,2,3],[3,2,1]]))
print(solution.maximumWealth([[1,5],[7,3],[3,5]]))
print(solution.maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))