class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if (dividend >= 0 and divisor > 0) or (dividend <= 0 and divisor < 0):
            share = dividend // divisor
            if share >= pow(2,31) - 1:
                share = pow(2,31) - 1
            return share
        else:
            if dividend < 0:
                dividend = abs(dividend)
            if divisor < 0:
                divisor = abs(divisor)
            share = dividend // divisor
            return -share

print(Solution().divide(7, -3))