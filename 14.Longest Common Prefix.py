class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        else:
            result = strs[0]
            for a in strs:
                result_list = list(result)
                length = len(result_list)
                a_list = list(a)
                common = []
                for i in range(length):
                    if i >= len(a_list):
                        break
                    if result_list[i] == a_list[i]:
                        common.append(result_list[i])
                    else:
                        break
                result = "".join(common)
            return result                

print(Solution().longestCommonPrefix(["flower","flow","flight"]))