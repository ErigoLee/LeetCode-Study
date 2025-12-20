class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_str = str(x)
        x_len_half = int(len(x_str)/2)
        x_len = len(x_str)
        result = True
        for i in range (x_len_half+1):
            if x_str[i] != x_str[x_len-1-i]:
                    result = False
                    break
        return result
print(Solution().isPalindrome(10))