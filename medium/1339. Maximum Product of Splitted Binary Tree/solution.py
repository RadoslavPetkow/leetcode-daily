# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7

        stack = [(root, 0)]
        subsum = {}
        sums = []

        while stack:
            node, seen = stack.pop()
            if not node:
                continue
            if not seen:
                stack.append((node, 1))
                stack.append((node.right, 0))
                stack.append((node.left, 0))
            else:
                s = node.val + subsum.get(node.left, 0) + subsum.get(node.right, 0)
                subsum[node] = s
                sums.append(s)

        total = subsum[root]
        best = 0
        for s in sums:
            best = max(best, s * (total - s))

        return best % MOD