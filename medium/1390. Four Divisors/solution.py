from typing import List
import math

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def is_prime(x: int) -> bool:
            if x < 2:
                return False
            if x % 2 == 0:
                return x == 2
            r = int(math.isqrt(x))
            for i in range(3, r + 1, 2):
                if x % i == 0:
                    return False
            return True

        ans = 0

        for n in nums:
            root = int(math.isqrt(n))
            found = False
            d1 = d2 = 0

            for d in range(2, root + 1):
                if n % d == 0:
                    if found:
                        d1 = 0
                        break
                    found = True
                    d1 = d
                    d2 = n // d

            if d1 == 0 or d1 == d2:
                continue

            if is_prime(d1) and is_prime(d2):
                ans += 1 + d1 + d2 + n

            elif is_prime(d1) and d2 == d1 * d1:
                ans += 1 + d1 + d2 + n

        return ans