class Solution(object): # TODO: This implementation is incorrect. ex) s = "()[]{}" output: False expected: True
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        map_parenthese = {'(':')','{':'}','[':']'}
        length = len(s)
        half = len(s)/2
        for i in range(half):
            c = s[i]
            if map_parenthese[c] != s[length - 1 - i]:
                return False
        return True
        