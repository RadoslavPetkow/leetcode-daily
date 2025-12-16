from typing import List

class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int],
                  hierarchy: List[List[int]], budget: int) -> int:

        children = [[] for _ in range(n)]
        for u, v in hierarchy:
            children[u - 1].append(v - 1)

        NEG_INF = -10**18

        dp0 = [[NEG_INF] * (budget + 1) for _ in range(n)]
        dp1 = [[NEG_INF] * (budget + 1) for _ in range(n)]

        def merge_knapsack(a: List[int], b: List[int]) -> List[int]:

            res = [NEG_INF] * (budget + 1)
            for i in range(budget + 1):
                if a[i] == NEG_INF:
                    continue

                for j in range(budget - i + 1):
                    if b[j] == NEG_INF:
                        continue
                    val = a[i] + b[j]
                    if val > res[i + j]:
                        res[i + j] = val
            return res

        def dfs(u: int) -> None:
            for v in children[u]:
                dfs(v)
            for pb in (0, 1):
                cur_not = [NEG_INF] * (budget + 1)
                cur_not[0] = 0
                for v in children[u]:
                    cur_not = merge_knapsack(cur_not, dp0[v])
                cost_u = present[u] if pb == 0 else (present[u] // 2)
                profit_u = future[u] - cost_u

                cur_buy = [NEG_INF] * (budget + 1)
                if cost_u <= budget:
                    cur_buy[cost_u] = profit_u

                for v in children[u]:
                    cur_buy = merge_knapsack(cur_buy, dp1[v])
                best = [max(cur_not[b], cur_buy[b]) for b in range(budget + 1)]
                if pb == 0:
                    dp0[u] = best
                else:
                    dp1[u] = best

        dfs(0)

        return max(dp0[0])