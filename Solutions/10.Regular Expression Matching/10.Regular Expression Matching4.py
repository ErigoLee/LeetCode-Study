class Solution(object):  ## Time Limit Exceeded
    def dp(self, s, p, i, j, memo):
        if len(p) == j:
            return s == memo

        if len(s) == i:
            while j < len(p):
                if j == len(p)-1:
                    return False
                else:
                    if p[j+1] == '*':
                        j = j + 2
                    else:
                        return False     
            return True
        if len(p) - 1 == j:
            if p[j] == '.':
                memo += s[i]
                return self.dp(s,p,i+1,j+1,memo) 
            else:
                memo += p[j]
                return self.dp(s,p,i+1,j+1,memo)
        else:
            if p[j] == s[i]:
                if p[j+1] =='*':
                    result = self.dp(s,p,i,j+2,memo)
                    if result == True:
                        return True
                    else:
                        memo += p[j]
                        return self.dp(s,p,i+1,j,memo) 
                else:
                    memo += p[j]
                    return self.dp(s,p,i+1,j+1,memo)
            elif p[j] == '.':
                if p[j+1] == '*':
                    result = self.dp(s,p,i,j+2,memo)
                    if result == True:
                        return True
                    else:
                        memo += s[i]
                        return self.dp(s,p,i+1,j,memo) 
                else:
                    memo += s[i]
                    return self.dp(s,p,i+1,j+1,memo)
            else:
                if p[j+1] == '*':
                    return self.dp(s,p,i,j+2,memo)
                else:
                    return False

        
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if p == ".*":
            return True
        else:
            return self.dp(s, p, 0, 0, "")

print(Solution().isMatch("aaaaaaaaaaaaaaaaaaab","a*a*a*a*a*a*a*a*a*a*"))