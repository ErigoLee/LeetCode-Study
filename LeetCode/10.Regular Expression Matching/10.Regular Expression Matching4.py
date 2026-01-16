class Solution(object): 
    def exp(self, s, p_list, i, memo, sharp_index, add_element):
        if len(memo) == len(s):
            memo_str = "".join(memo)
            if memo_str == p:
                return True
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
            p_list = list(p)
            sharp_index = []
            memo = []
            normal_index = []
            add_element = []
            index = 0
            for i in p_list:
                if i == "*":
                    sharp_index.append(index)
                    add_element.append(p_list[index -1])
                else:
                    if index < len(p_list)-1:
                        if p_list[index +1] != "*":
                            memo.append(i)
                    else:
                        memo.append(i)
                index += 1
            print(sharp_index)
            print(memo)
            print(add_element)
            return self.exp(s, p_list, 0, memo, sharp_index, add_element)

print(Solution().isMatch("aaa","ab*a*c*a"))