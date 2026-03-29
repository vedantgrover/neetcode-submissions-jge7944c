class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxSolution: int = 0;

        l = 0

        cur = 0
        for r in range(1,len(prices)):
            cur = prices[r] - prices[l]
            while cur < 0:
                l += 1
                cur = prices[r] - prices[l]


            maxSolution = max(maxSolution, cur)

        

        return maxSolution;