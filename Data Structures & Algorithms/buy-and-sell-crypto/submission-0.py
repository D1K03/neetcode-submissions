class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left,right = 0, 1
        maxProf = 0

        while right < len(prices):
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                maxProf = max(maxProf, profit)
            else:
                left = right
            right += 1
        
        return maxProf       