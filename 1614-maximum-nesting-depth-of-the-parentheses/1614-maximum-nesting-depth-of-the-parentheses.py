class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        open = 0
        l = len(s)
        for i in range(l):
            if s[i] == '(':
                open+=1
            if s[i] == ')':
                open -=1
            ans = max(open,ans)
        return ans
        