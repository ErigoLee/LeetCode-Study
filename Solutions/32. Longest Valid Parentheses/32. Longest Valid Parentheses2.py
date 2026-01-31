class Solution(object):
    def longestValidParentheses(self, s): # wrong answer - )(()(()(((())(((((()()))((((()()(()()())())())()))()()()())(())()()(((()))))()((()))(((())()((()()())((())))(())))())((()())()()((()((())))))((()(((((()((()))(()()(())))((()))()))())
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0
        start = 0
        candidates = []
        for i in range(len(s)):
            if s[i] == '(':
                left = left + 1
            else:
                right = right + 1
                if left <= 0:
                    right = 0
                    start = i + 1
                else:
                    if right > left:
                        print("left:", left, " right:", right)
                        candidates.append(s[i-(left*2-1):i+1])
                    elif right == left:
                        candidates.append(s[start:i+1])
                        right = 0
                        left = 0
                    else:
                        print("left:", left, " right:", right)
                        ss = s[i-(right*2-1):i+1]
                        _left = 0
                        _right = 0
                        _start = 0
                        for j in range(len(ss)):
                            if ss[j] == '(':
                                _left = _left + 1
                            else:
                                _right = _right + 1
                                if _left <= 0:
                                    _right = 0
                                    _start = j + 1
                                else:
                                    if _right > _left:
                                        candidates.append(ss[j-(_left*2-1):j+1])
                                    elif _right == _left:
                                        candidates.append(ss[_start:j+1])
                                        _right = 0
                                        _left = 0
                                    else:
                                        candidates.append(ss[j-(_right*2-1):j+1])
                        ##candidates.append(s[i-(right*2-1):i+1])
        
        result = ""
        for a in candidates:
            print(a)
            if len(a) > len(result):
                result = a
        return len(result)

print(Solution().longestValidParentheses(")(()(()(((())(((((()()))((((()()(()()())())())()))()()()())(())()()(((()))))()((()))(((())()((()()())((())))(())))())((()())()()((()((())))))((()(((((()((()))(()()(())))((()))()))())"))
      
        
        