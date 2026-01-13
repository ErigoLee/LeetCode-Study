class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        map_parenthese = {')':'(','}':'{',']':'['}
        key_list = [')','}',']']
        value_list = ['(','{','[']
        stack = []
        for i in range(len(s)):
            if s[i] in value_list:
                stack.append(s[i])

            if s[i] in key_list:
                if len(stack) == 0:
                    return False
                else:
                    c = stack.pop()
                if c != map_parenthese[s[i]]:
                    return False 
        
        if len(stack) == 0:
            return True
        else:
            return False

print(Solution().isValid("([])")) # True