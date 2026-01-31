class Solution(object):
    def longestValidParentheses(self, s):
        stack = [-1]  # 마지막으로 "유효 시작"을 막는 기준 인덱스
        best = 0

        for i, ch in enumerate(s):
            print("i:", i, " ch:", ch, " stack:", stack)
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    # 짝이 없는 ')' -> 새로운 기준점
                    stack.append(i)
                else:
                    # 현재 i에서 끝나는 유효 길이
                    best = max(best, i - stack[-1])

        return best

print(Solution().longestValidParentheses(")(()(()(((())(((((()()))((((()()(()()())())())()))()()()())(())()()(((()))))()((()))(((())()((()()())((())))(())))())((()())()()((()((())))))((()(((((()((()))(()()(())))((()))()))())"))
