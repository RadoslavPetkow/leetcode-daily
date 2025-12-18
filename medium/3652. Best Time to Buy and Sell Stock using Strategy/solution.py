from typing import List

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        h = k // 2

        base = 0
        for p, s in zip(prices, strategy):
            base += s * p

        A = [0] * n
        for i in range(n):
            A[i] = -strategy[i] * prices[i]

        B = [0] * n
        for i in range(n):
            B[i] = (1 - strategy[i]) * prices[i]

        prefA = [0] * (n + 1)
        prefB = [0] * (n + 1)
        for i in range(n):
            prefA[i + 1] = prefA[i] + A[i]
            prefB[i + 1] = prefB[i] + B[i]

        best_delta = 0
        for l in range(0, n - k + 1):
            first_half_delta = prefA[l + h] - prefA[l]
            second_half_delta = prefB[l + k] - prefB[l + h]
            delta = first_half_delta + second_half_delta
            if delta > best_delta:
                best_delta = delta

        return base + best_delta