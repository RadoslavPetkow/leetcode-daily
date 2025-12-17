from typing import List

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        if n < 2 or k == 0:
            return 0

        dpPrev = [0] * n

        for _ in range(1, k + 1):
            dpCur = [0] * n

            bestLong = -prices[0]
            bestShort = prices[0]

            for j in range(1, n):
                dpCur[j] = dpCur[j - 1]

                endProfit = max(prices[j] + bestLong, -prices[j] + bestShort)
                if endProfit > dpCur[j]:
                    dpCur[j] = endProfit

                prevBeforeStart = dpPrev[j - 1]
                bestLong = max(bestLong, prevBeforeStart - prices[j])
                bestShort = max(bestShort, prevBeforeStart + prices[j])

            dpPrev = dpCur

        return dpPrev[-1]