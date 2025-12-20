class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        temp = abs(x)
        x_str = str(temp)
        x_reverse = x_str[::-1]
        result = int(x_reverse)
        if x < 0:
            result = 0 - result
        
        if result > pow(2,31) or result < pow(-2,31):
            return 0
        else:
            return result

print(Solution().reverse(-123))