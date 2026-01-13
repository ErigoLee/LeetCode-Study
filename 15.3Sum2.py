class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    temp = [nums[i],nums[left],nums[right]]
                    temp.sort()
                    if not temp in result:
                        result.append(temp)
                    left = left + 1
                    right = right - 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left = left + 1
                else:
                    right = right - 1
        return result
print(Solution().threeSum([-1,0,1,2,-1,-4]))