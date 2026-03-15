class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        count = 0
        smap = set()
        fast = 0
        slow = 0
        l = len(s)
        while fast < l:
            if s[fast] not in smap:
                count += 1
                smap.add(s[fast])
                ans = max(ans,count)
                fast += 1
            else:
                smap.clear()
                count = 0
                slow += 1
                fast = slow
        return ans