class Solution(object):
    def lengthOfLongestSubstring(self, s):
        substrlist = []
        length = len(s)
        maxlen = 0
        for i in range(length):
            substr = ""
            for j in range(i, length):
                if s[j] not in substr:
                    substr += s[j]
                else:
                    break
            if len(substr) > maxlen:
                maxlen = len(substr)
            substrlist.append(substr)
        print(substrlist)
        return maxlen
print(Solution().lengthOfLongestSubstring("abcabcbb"))