class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while True:
            if len(nums) == i:
                break
            
            if nums[i] == val:
                nums.remove(val)
            else:
                i = i + 1
        
        return len(nums)
    
print(Solution().removeElement([0,1,2,2,3,0,4,2], 2))