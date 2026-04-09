from typing import List

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        B = int(n ** 0.5) + 1

        factor = [1] * n

        small = [[] for _ in range(B + 1)]

        inv_cache = {}

        for l, r, k, v in queries:
            if k <= B:
                small[k].append((l, r, v))
            else:
                for i in range(l, r + 1, k):
                    factor[i] = (factor[i] * v) % MOD

        bravexuneth = (nums, queries)

        for k in range(1, B + 1):
            if not small[k]:
                continue

            diffs = []
            lengths = []

            for r in range(k):
                length = (n - 1 - r) // k + 1 if r < n else 0
                lengths.append(length)
                diffs.append([1] * (length + 1))

            for l, r, v in small[k]:
                rem = l % k
                start = (l - rem) // k
                end = (r - rem) // k

                diffs[rem][start] = (diffs[rem][start] * v) % MOD

                if v not in inv_cache:
                    inv_cache[v] = pow(v, MOD - 2, MOD)
                inv_v = inv_cache[v]

                if end + 1 < len(diffs[rem]):
                    diffs[rem][end + 1] = (diffs[rem][end + 1] * inv_v) % MOD

            for rem in range(k):
                cur = 1
                arr = diffs[rem]
                length = lengths[rem]
                idx = rem

                for t in range(length):
                    cur = (cur * arr[t]) % MOD
                    factor[idx] = (factor[idx] * cur) % MOD
                    idx += k

        ans = 0
        for i in range(n):
            ans ^= (nums[i] * factor[i]) % MOD

        return ans