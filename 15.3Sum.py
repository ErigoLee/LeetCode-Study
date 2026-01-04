class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        for i in range (0,len(nums)-2):
            for j in range (i+1, len(nums)-1):
                for k in range (j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp = [nums[i], nums[j], nums[k]]
                        temp.sort()
                        if not temp in result:
                            result.append(temp)
        return result
print(Solution().threeSum([-1,0,1,2,-1,-4]))