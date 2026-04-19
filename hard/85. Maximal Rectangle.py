class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for row in matrix:
            for i in range(cols):
                if row[i] == "1":
                    heights[i] += 1
                else:
                    heights[i] = 0

            max_area = max(max_area, self.largestRecArea(heights))

        return max_area

    def largestRecArea(self, heights):
        stack = []
        max_area = 0
        arr = heights + [0]

        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                h = arr[stack.pop()]
                left = stack[-1] if stack else -1
                width = i - left - 1
                max_area = max(max_area,  h* width)
            stack.append(i)

        return max_area

