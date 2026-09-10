class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        minPrice=prices[0]
        for i in range(len(prices)):
            currentProfit = prices[i] - minPrice
            maxProfit = max(currentProfit,maxProfit)
            minPrice = min(minPrice,prices[i])
        return maxProfit

        