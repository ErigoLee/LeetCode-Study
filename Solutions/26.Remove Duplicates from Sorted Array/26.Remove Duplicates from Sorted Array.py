class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = []
        nums.sort()
        prev_value = -101
        i = 0
        while True:
            if i == len(nums):
                break

            if nums[i] > prev_value:
                prev_value = nums[i]
                i = i + 1
                
            else:
                a = nums[i]
                nums.remove(a)

        return len(nums)

print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))