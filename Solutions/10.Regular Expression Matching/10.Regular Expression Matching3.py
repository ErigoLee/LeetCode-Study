class Solution(object): # Dynamic Programming 
    def dp(self, s, p, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]
        if j == len(p):
            return i == len(s)
        first_match = i < len(s) and p[j] in {s[i], '.'}
        if j + 1 < len(p) and p[j + 1] == '*':
            ans = self.dp(s, p, i, j + 2, memo) or first_match and self.dp(s, p, i + 1, j, memo)
        else:
            ans = first_match and self.dp(s, p, i + 1, j + 1, memo)
        memo[(i, j)] = ans
        print(memo)
        return ans
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if p == ".*":
            return True
        else:
            return self.dp(s, p, 0, 0, {})
        
print(Solution().isMatch("aaa","ab*a*c*a"))