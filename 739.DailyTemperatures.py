from typing import List

# Monotionic decreasing stack
#BigO (n) strictly (2 * n)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # we will store each individual as [temperature, index]

        for i, t in enumerate(temperatures):

            # while stack is not null and temperature is greater than the last one
            print("i", i, "t", t)
            while stack and t > stack[-1][1]:
                stackInd, stackT = stack.pop()
                print("Popping------->", "stackInd", stackInd, "stackT", stackT)
                res[stackInd] = i - stackInd
                print("res", res)
            stack.append([i, t])
            print("stack", stack)
            print("-----")

        return res 

temperatures = [[73,74,75,71,69,72,76,73],[30,40,50,60],[30,60,90]]
for i in temperatures:
    sol = Solution().dailyTemperatures(i)
    print(sol)