class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        left,right = 0,0
        ans = 0
        while left < len(g) and right < len(s):
            if g[left] <= s[right]:
                ans += 1
                right += 1
                left+= 1
            right += 1
        return ans
        