from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        deletions = 0

        for col in range(m):
            for row in range(n - 1):
                if strs[row][col] > strs[row + 1][col]:
                    deletions += 1
                    break

        return deletions