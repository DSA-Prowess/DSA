class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left, right = 0,1 
        maxP = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxP = max( maxP, profit)
            else:
                left = right  # found new minima istead of iterating and checking 
            right +=1
        return maxP








if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    obj = Solution()
    res = obj.maxProfit(prices)
    print(res)
