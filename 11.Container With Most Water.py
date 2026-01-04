class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                row = j - i
                col = 0
                if height[i] > height[j]:
                    col = height[j]
                else:
                    col = height[i]
                shape = row * col
                if shape > result:
                    result = shape
        return result

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))