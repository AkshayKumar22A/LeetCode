class Solution:
    def longestPalindrome(self, s: str) -> str:
        best_len = 0
        best_s = ""

        for mid in range(len(s)):
            x = 0
            while (mid - x) >= 0 and (mid + x) < len(s):
                if s[mid-x] != s[mid+x]:
                    break
                l = 2 * x + 1
                if l > best_len:
                    best_len = l
                    best_s = s[mid-x:mid+x+1]
                x+=1 

        for mid in range(len(s)-1):
            x = 1
            while (mid - x + 1) >= 0 and (mid + x) < len(s):
                if s[mid-x+1] != s[mid+x]:
                    break
                l = 2 * x
                if l > best_len:
                    best_len = l
                    best_s = s[mid-x+1:mid+x+1]
                x += 1

        return best_s