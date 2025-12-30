from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        if r < 3 or c < 3:
            return 0

        def is_magic(x: int, y: int) -> bool:
            if grid[x + 1][y + 1] != 5:
                return False

            nums = []
            seen = set()
            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    v = grid[i][j]
                    if v < 1 or v > 9 or v in seen:
                        return False
                    seen.add(v)
                    nums.append(v)

            s = grid[x][y] + grid[x][y + 1] + grid[x][y + 2]

            if grid[x + 1][y] + grid[x + 1][y + 1] + grid[x + 1][y + 2] != s:
                return False

            if grid[x + 2][y] + grid[x + 2][y + 1] + grid[x + 2][y + 2] != s:
                return False

            if grid[x][y] + grid[x + 1][y] + grid[x + 2][y] != s:
                return False

            if grid[x][y + 1] + grid[x + 1][y + 1] + grid[x + 2][y + 1] != s:
                return False

            if grid[x][y + 2] + grid[x + 1][y + 2] + grid[x + 2][y + 2] != s:
                return False

            if grid[x][y] + grid[x + 1][y + 1] + grid[x + 2][y + 2] != s:
                return False

            if grid[x][y + 2] + grid[x + 1][y + 1] + grid[x + 2][y] != s:
                return False

            return True

        ans = 0
        for i in range(r - 2):
            for j in range(c - 2):
                if is_magic(i, j):
                    ans += 1
        return ans