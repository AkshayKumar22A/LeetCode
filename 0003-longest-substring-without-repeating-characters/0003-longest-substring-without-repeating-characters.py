class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        smap = {}
        slow = 0
        fast = 0
        while fast < len(s):
            if s[fast] in smap:
                slow = max(slow,smap[s[fast]]+1)
            ans = max(ans,fast-slow+1)
            smap[s[fast]] = fast
            fast += 1
        return ans