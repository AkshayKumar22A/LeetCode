class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = " ".join(s.split())
        ans = s.split(" ")
        return len(ans[-1])
        
        