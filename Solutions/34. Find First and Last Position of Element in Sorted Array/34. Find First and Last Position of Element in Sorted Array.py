class Solution(object):
    def binaray(self,min_idx,max_idx,target,nums):
        start_idx = 10000000000
        end_idx = -1 
        while min_idx <= max_idx:
            mid = (min_idx+max_idx)//2
            if nums[mid] > target:
                max_idx = max_idx - 1
            elif nums[mid] < target:
                min_idx = min_idx + 1
            else:
                if start_idx > mid:
                    start_idx = mid
                if end_idx < mid:
                    end_idx = mid
        
        if end_idx == -1:
            return [-1, -1]
        else:
            return [start_idx, end_idx]


    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        min_idx = 0
        max_idx = len(nums)-1
        result = self.binaray(min_idx,max_idx,target,nums)
        return result

print(Solution().searchRange([5,7,7,8,8,10],8))