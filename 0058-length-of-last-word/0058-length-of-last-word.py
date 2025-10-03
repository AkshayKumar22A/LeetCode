class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        li = " ".join(s.split())
        ans = li.split(" ")
        return len(ans[-1])
        
        