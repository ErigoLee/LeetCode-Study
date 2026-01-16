class Solution(object):
    def dp(self, digits, place, length, memo, map_num_alphbet):
        if place == length:
            return memo
        
        digit = digits[place]
        length_alphbet = len(map_num_alphbet[digit])
        result = []
        for i in range(length_alphbet):
            renew_memo = memo + map_num_alphbet[digit][i]
            temp = self.dp(digits,place+1,length, renew_memo, map_num_alphbet)
            if temp != None:
                if type(temp) == list:
                    for j in temp:
                        result.append(j)
                else:
                    result.append(temp)
        
        return result
        

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        map_num_alphbet = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}

        result = self.dp(digits,0, len(digits), '', map_num_alphbet)
        
        return result

print(Solution().letterCombinations("234"))