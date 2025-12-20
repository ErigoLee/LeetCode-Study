class Solution(object):
    def longestPalindrome(self, s):      
        storedStr = []
        for i in range(len(s)):
            a = []
            for j in range(len(s)-1, i, -1):
                if s[i] == s[j]:
                    a.append(j)
            a_remove = []
            if len(a) != 0:
                for a_index in a:
                    for t in range(i+1,a_index,1):
                        if s[t] != s[a_index-(t-i)]:
                            a_remove.append(a_index)
                            break
            for r in a_remove:
                a.remove(r)
            
            if len(a) != 0:
                for a_index in a:
                    storedStr.append(s[i:a_index+1])
        if len(storedStr) == 0:
            return s[0]
        else:
            result = ""
            max_len = 0
            for a in storedStr:
                if len(a) > max_len:
                    result = a
                    max_len = len(a)
            return result

print(Solution().longestPalindrome("aacabdkacaa"))