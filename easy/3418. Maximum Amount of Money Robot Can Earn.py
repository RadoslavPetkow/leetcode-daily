from typing import List

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        NEG_INF = float("-inf")

        # dp[i][j][k] = max coins at cell (i, j) using exactly k neutralizations
        dp = [[[NEG_INF] * 3 for _ in range(n)] for _ in range(m)]

        # Base case: start cell
        start = coins[0][0]
        dp[0][0][0] = start
        if start < 0:
            dp[0][0][1] = 0  # neutralize the robber at the start

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                val = coins[i][j]

                for k in range(3):
                    best_prev = NEG_INF

                    # Come from top
                    if i > 0:
                        best_prev = max(best_prev, dp[i - 1][j][k])

                    # Come from left
                    if j > 0:
                        best_prev = max(best_prev, dp[i][j - 1][k])

                    # Option 1: do not neutralize this cell
                    if best_prev != NEG_INF:
                        dp[i][j][k] = max(dp[i][j][k], best_prev + val)

                    # Option 2: neutralize this cell (only if negative and k > 0)
                    if val < 0 and k > 0:
                        best_prev_neutralized = NEG_INF

                        if i > 0:
                            best_prev_neutralized = max(best_prev_neutralized, dp[i - 1][j][k - 1])
                        if j > 0:
                            best_prev_neutralized = max(best_prev_neutralized, dp[i][j - 1][k - 1])

                        if best_prev_neutralized != NEG_INF:
                            dp[i][j][k] = max(dp[i][j][k], best_prev_neutralized)

        return max(dp[m - 1][n - 1])