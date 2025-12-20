class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        newList = nums1
        for num in nums2:
            if num is not newList:
                newList.append(num)
        newList.sort()
        median = 0
        if len(newList) % 2 == 0:
            median = (newList[int(len(newList)/2)] + newList[int(len(newList)/2-1)])/2
        else:
            median = newList[int(len(newList)/2)]
        return median
        
print(Solution().findMedianSortedArrays([1,3],[2,4]))