from tkinter import N


class Solution:
    def isHappy(self, n: int) -> bool:
        if n < 10:
            return False
        

sol = Solution().isHappy(19)
print(sol)