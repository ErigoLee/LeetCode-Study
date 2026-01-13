class Solution(object):
    
    def makingParenthesis(self, m, p, n, memo):
        
        
        if m == 0 and p == n:
            return memo
        
        if m > 0 and p == n:
            return self.makingParenthesis(m-1, p, n, memo + ')')
        if p == 0 and m == 0 and n != 0:
            return self.makingParenthesis(m+1, p+1, n, '(')
        
        if m > 0 and p < n:
            result = []
            if type(self.makingParenthesis(m+1, p+1, n, memo+'(')) == str:
                result.append(self.makingParenthesis(m+1, p+1, n, memo+'('))
            else:
                for i in self.makingParenthesis(m+1, p+1, n, memo+'('):
                    result.append(i)
            
            
            if type(self.makingParenthesis(m-1, p, n, memo+')')) == str:
                result.append(self.makingParenthesis(m-1, p, n, memo+')'))
            else:
                for i in self.makingParenthesis(m-1, p, n, memo+')'):
                    result.append(i)
            return result
        if m == 0 and p < n:
            return self.makingParenthesis(m+1, p+1, n, memo+'(')
                
        return None
    
    
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = self.makingParenthesis(0,0,n,"")
        
        if result == None:
            return []
        elif type(result) == str:
            return [result]
        else:
            return result


print(Solution().generateParenthesis(1))