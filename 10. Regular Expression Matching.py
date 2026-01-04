class Solution(object): # Only handles simple cases 
                        # for example s = "aa" and p = "a*"
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not "*" in p:
            if s == p:
                return True
            else:
                return False
        else:
            if "." in p:
                return True
            else:
                elements = list(s[:len(s)])
                for e in elements:
                    if not e in s:
                        return False
                return True

print(Solution().isMatch("aa","a*"))