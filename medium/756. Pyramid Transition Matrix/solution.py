from functools import lru_cache
from collections import defaultdict
from typing import List

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        nxt = defaultdict(list)
        for a in allowed:
            nxt[a[0] + a[1]].append(a[2])

        @lru_cache(None)
        def can_build(row: str) -> bool:
            if len(row) == 1:
                return True

            def build_next(i: int, path: List[str]) -> bool:
                if i == len(row) - 1:
                    return can_build("".join(path))

                pair = row[i] + row[i + 1]
                if pair not in nxt:
                    return False

                for ch in nxt[pair]:
                    path.append(ch)
                    if build_next(i + 1, path):
                        return True
                    path.pop()
                return False

            return build_next(0, [])

        return can_build(bottom)