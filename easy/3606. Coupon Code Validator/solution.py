from typing import List
import re

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        order = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}
        valid_code = re.compile(r"^[A-Za-z0-9_]+$")

        good = []
        for c, b, active in zip(code, businessLine, isActive):
            if not active:
                continue
            if b not in order:
                continue
            if not c or not valid_code.match(c):
                continue
            good.append((order[b], c))

        good.sort()
        return [c for _, c in good]