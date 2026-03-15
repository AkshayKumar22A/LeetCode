class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            myset = set()
            for j in range(i,len(s)):
                if s[j] in myset:
                    break
                ans = max(ans,j-i+1)
                myset.add(s[j])
        return ans