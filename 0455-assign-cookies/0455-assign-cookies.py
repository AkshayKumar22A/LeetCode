class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        left = 0
        right = 0
        ans = 0
        while left < len(g) and right < len(s):
            if g[left] <= s[right]:
                ans += 1
                right += 1
                left+= 1
            elif g[left] >= s[right]:
                right += 1
        return ans
        