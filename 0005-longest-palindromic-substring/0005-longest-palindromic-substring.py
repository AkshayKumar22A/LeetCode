class Solution:
    def is_palindrome(self,subs):
        rev = subs[::-1]
        return rev == subs
    
    def longestPalindrome(self, s: str) -> str:
        best_len = 0
        best_s = ""
    
        for i in range(len(s)):
            for j in range(i,len(s)):
                l = j-i+1
                subs = s[i:j+1]
                
                if l > best_len and self.is_palindrome(subs):
                    best_len = l
                    best_s = subs
        return best_s