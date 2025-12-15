class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = 0
        length = 1  # current smooth descent streak length
        ans += length

        for i in range(1, len(prices)):
            if prices[i - 1] - prices[i] == 1:
                length += 1
            else:
                length = 1
            ans += length

        return ans