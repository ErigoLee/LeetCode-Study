class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        candidates = []
        stack = []
        parenthese = ""
        for i in range(len(s)):
            if s[i] == '(':
                stack.append('(')
                parenthese += '('
            else:
                if len(stack) > 0:
                    stack.pop()
                    parenthese += ')'
                    
                else:
                    if len(parenthese) != 0:
                        candidates.append(parenthese)
                        parenthese = ""
        
        
        while len(stack) > 0 and len(parenthese) > 0:
            stack.pop()
            parenthese = parenthese[1:len(parenthese)]
        
        if len(parenthese) >0:
            candidates.append(parenthese)
        
        if len(candidates) == 0:
            return 0
        else:
            result = len(candidates[0])
            for p in candidates:
                if len(p) > result:
                    result = len(p)
            return result


print(Solution().longestValidParentheses("()(()"))