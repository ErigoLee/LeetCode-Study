class Solution(object): # this function is incomplete (ex: s = "aaa", p = "ab*a*c*a" returns False - actually True)
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if p == ".*":
            return True
        else:
            s_index = 0
            p_index = 0
            while s_index < len(s) and p_index < len(p):
                if p[p_index] == ".":
                    s_index += 1
                    p_index += 1
                elif p[p_index] == "*":
                    print("a")
                    if p[p_index -1] == ".":
                        s_index += 1
                    else:
                        print("b")
                        while s_index < len(s) and s[s_index] == p[p_index -1]:
                            s_index += 1
                        if s_index == len(s) and p_index + 2 == len(p):
                            if p[p_index+1] == s[s_index-1]:
                                return True
                            else:
                                while p_index +2 < len(p):
                                    if p[p_index +2] == "*":
                                        p_index += 2
                                    else:
                                        return False
                        else:
                            p_index += 1
                else:
                    if s[s_index] == p[p_index]:
                        print("c")
                        s_index += 1
                        p_index += 1
                    elif p[p_index + 1] == "*":
                        print("d")
                        p_index += 2
                    else:
                        print("e")
                        return False
        if s_index != len(s):
            print("k")
            return False
        elif p_index != len(p):
            print("l")
            return False
        else:
            print("m")
            return True

print(Solution().isMatch("aaa","ab*a*c*a"))