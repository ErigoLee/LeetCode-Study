class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            while left < right:
                temp = nums[i]+nums[left] +nums[right]
                compared_result_target = abs(result-target)
                compared_temp_target = abs(temp-target)
                if compared_temp_target < compared_result_target:
                    result = temp
                if temp < target:
                    left = left + 1
                elif temp > target:
                    right = right - 1
                else:
                    return target
        return result

print(Solution().threeSumClosest([-84,92,26,19,-7,9,42,-51,8,30,-100,-13,-38],78))