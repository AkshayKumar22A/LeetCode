class Solution:
    def maxDepth(self, s: str) -> int:
        open = 0
        close = 0
        ans = 0
        l = len(s)
        for i in range(l):
            if s[i] == '(':
                open+=1
            if s[i] == ')':
                close +=1
            ans = max(ans,(open-close))
        return ans
        