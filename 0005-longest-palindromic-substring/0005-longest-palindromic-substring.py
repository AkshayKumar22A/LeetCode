class Solution:
    def is_palindrome(self,subs):
        return subs == subs[::-1]

    def good(self,x,s):
        for i in range(len(s) - x + 1):
            if self.is_palindrome(s[i:i+x]):
                return i
        return -1    

    
    def longestPalindrome(self, s: str) -> str:
        best_len = 0
        best_s = ""

        for parity in [0, 1]:
            low, high = 1, len(s)

            if low % 2 != parity:
                low += 1
            if high % 2 != parity:
                high -= 1
        
            while low <= high:
                mid = (low + high) // 2
                if mid % 2 != parity:
                    mid += 1
                if mid > high:
                    break

                temp = self.good(mid,s)
                if temp != -1:
                    if mid > best_len:
                        best_len = mid
                        best_s = s[temp:temp+mid]
                    low = mid + 2
                else:
                    high = mid - 2

        return best_s