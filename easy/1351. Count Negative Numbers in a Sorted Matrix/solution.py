from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum(1 for row in grid for x in row if x < 0)