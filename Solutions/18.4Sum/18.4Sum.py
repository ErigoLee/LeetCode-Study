class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum == target:
                        temp = [nums[i], nums[j],nums[left], nums[right]]
                        if not temp in result:
                            result.append(temp)
                        left = left + 1
                        right = right - 1
                    elif sum < target:
                        left = left + 1
                    else:
                        right = right - 1
        return result

print(Solution().fourSum([1,0,-1,0,-2,2],0))