class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        negative = False
        result = ""
        for i in range(len(s)):
            if i == 0 and (s[i] == '-' or s[i] == '+'):
                if s[i] == '-':
                    negative = True
                continue
            if s[i] >= '0' and s[i] <= '9':
                result += s[i]
            else:
                break
        if len(result) == 0:
            return 0
        else:
            if negative == True:
                result_int = 0 - int(result)
                if result_int < pow(-2, 31):
                    return pow(-2,31)
                return result_int
            else:
                result_int = int(result)
                if result_int > pow(2,31) - 1:
                    return pow(2,31) - 1
                return result_int

print(Solution().myAtoi("words and 987"))