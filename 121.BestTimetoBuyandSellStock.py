# def maxProfit(prices):
#     profit = 0
#     buy = prices[0]
#     sell = prices[1]
#     for i in prices[2:]:
#         if sell < i:
#             sell = i
#     if buy < sell:
#         profit = sell - buy
#         return profit
#     else:
#         return 0


# print(maxProfit([7,1,5,3,6,4]))

#=======================================
# def maxProfit(prices):
#     profit = 0
#     buy = prices[0]
#     i = 0
#     buy_iter = 0
#     while i < len(prices):
#         if buy > prices[i]:
#             buy = prices[i]
#             buy_iter = i
#         i += 1

#     sell_list = prices[buy_iter:]
#     sell = sell_list[0]
#     for j in sell_list:
#         if sell < j:
#             sell = j

#     # profit
#     print("buy: ", buy)
#     print("sell: ", sell)
#     if buy < sell:
#         profit = sell - buy
#         return profit
#     else:
#         return 0

#=================================================

#Correct Solution
def maxProfit(prices):
    left, right = 0, 1 # buy = left, sell = right
    max_profit = 0 
    while right < len(prices):
        if prices[left] < prices[right]:
            current_profit = prices[right] - prices[left]
            max_profit = max(max_profit, current_profit)
        else:
            left = right
        right += 1
    return max_profit


# testcases
prices1 = [7,1,5,3,6,4]
prices2 = [7,6,4,3,1]
prices3 = [2,4,1]
print(maxProfit(prices1))
print(maxProfit(prices2))
print(maxProfit(prices3))