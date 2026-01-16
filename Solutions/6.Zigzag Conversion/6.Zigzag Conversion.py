class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        
        rows = []
        for i in range(numRows):
            rows.append("")
        
        up = True
        index = 0
        for i in range(len(s)):
            if up:
                rows[index] += s[i]
                if index == numRows - 1:
                    up = False
                    index = index - 1
                else:
                    index = index + 1
            else:
                rows[index] += s[i]
                if index == 0:
                    up = True
                    index = index + 1
                else:
                    index = index - 1
        result = ""
        for r in rows:
            result += r
        return result
                


print(Solution().convert("PAYPALISHIRING",4))