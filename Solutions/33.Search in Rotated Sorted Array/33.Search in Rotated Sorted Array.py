class Solution(object):
    def binarySearch(self,min_idx,max_idx,target,nums):

        flag = False
        nums_max_idx = len(nums)-1
        
        while min_idx != max_idx:
            if max_idx == nums_max_idx or min_idx == 0:
                flag = True
            
            if flag == True:
                mid = (max_idx+min_idx)//2
                if nums[mid] > target:
                    max_idx = max_idx - 1
                    if max_idx == -1:
                        max_idx = nums_max_idx
                elif nums[mid] < target:
                    min_idx = min_idx + 1
                    if min_idx == len(nums):
                        min_idx = 0
                else:
                    return mid
            else:
                mid = (min_idx-max_idx)//2
                if nums[mid] > target:
                    max_idx = max_idx - 1
                    if max_idx == -1:
                        max_idx = nums_max_idx
                elif nums[mid] < target:
                    min_idx = min_idx + 1
                    if min_idx == len(nums):
                        min_idx = 0
                else:
                    return mid
        
        if min_idx == max_idx and nums[min_idx] == target:
            return min_idx
        else:
            return -1

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        max_num = max(nums)
        max_idx = nums.index(max_num)
        min_num = min(nums)
        min_idx = nums.index(min_num)
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        else:
            if target > max_num or target < min_num:
                return -1
            else:
                result = self.binarySearch(min_idx,max_idx,target,nums)
                return result
  

print(Solution().search([4,5,6,7,0,1,2], 6))