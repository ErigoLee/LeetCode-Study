class Solution(object):  ## Fixed (no TLE)
    def dp(self, s, p, i, j, cache):
        if (i, j) in cache:
            return cache[(i, j)]

        if len(p) == j:
            result = (len(s) == i)
            cache[(i, j)] = result
            return result

        if len(s) == i:
            jj = j 
            while jj < len(p):
                if jj == len(p) - 1:
                    cache[(i, j)] = False
                    return False
                else:
                    if p[jj + 1] == '*':
                        jj = jj + 2
                    else:
                        cache[(i, j)] = False
                        return False
            cache[(i, j)] = True
            return True

        if len(p) - 1 == j:
            result = False
            if p[j] == '.' or p[j] == s[i]:
                result = self.dp(s, p, i + 1, j + 1, cache)
            else:
                result = False
            cache[(i, j)] = result
            return result

        if p[j] == s[i]:
            if p[j + 1] == '*':
                result = self.dp(s, p, i, j + 2, cache)
                if result == True:
                    cache[(i, j)] = True
                    return True
                else:
                    result2 = self.dp(s, p, i + 1, j, cache)
                    cache[(i, j)] = result2
                    return result2
            else:
                result = self.dp(s, p, i + 1, j + 1, cache)
                cache[(i, j)] = result
                return result

        elif p[j] == '.':
            if p[j + 1] == '*':
                result = self.dp(s, p, i, j + 2, cache)
                if result == True:
                    cache[(i, j)] = True
                    return True
                else:
                    result2 = self.dp(s, p, i + 1, j, cache)
                    cache[(i, j)] = result2
                    return result2
            else:
                result = self.dp(s, p, i + 1, j + 1, cache)
                cache[(i, j)] = result
                return result

        else:
            if p[j + 1] == '*':
                result = self.dp(s, p, i, j + 2, cache)
                cache[(i, j)] = result
                return result
            else:
                cache[(i, j)] = False
                return False

    def isMatch(self, s, p):
        if p == ".*":
            return True
        else:
            return self.dp(s, p, 0, 0, {})


print(Solution().isMatch("aaaaaaaaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*"))
