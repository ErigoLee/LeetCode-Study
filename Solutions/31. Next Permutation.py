class Solution(object):
   
    
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        
        i = len(nums)-2
        pivot = -1
        while i >=0 and nums[i] >= nums[i+1]:
            i = i - 1
        pivot = i
        print(pivot)
        if pivot == -1:
            return nums.sort()
        else:
            threshold = 101
            change_idx = -1
            for j in range(pivot+1, len(nums)):
                if threshold > nums[j] and nums[j] > nums[pivot]:
                    change_idx = j
            if change_idx != -1:
                temp = nums[pivot]
                nums[pivot] = nums[change_idx]
                nums[change_idx] = temp
                nums[pivot+1:] = sorted(nums[pivot+1:])
        
        return nums
print(Solution().nextPermutation([1,3,2]))