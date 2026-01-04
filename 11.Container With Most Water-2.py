class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        half = len(height)//2
        left = 0
        right = len(height)-1
        result = 0
        while left <= len(height)-1 and right >= 0:
            if result < (right - left) * min(height[left], height[right]):
                result = (right - left) * min(height[left], height[right])
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return result
        
print(Solution().maxArea([8,7,2,1]))