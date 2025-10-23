class Solution:
    def hasSameDigits(self, s: str) -> bool:

        while len(s) != 2:
            l = len(s)
            ans = ""
            for i in range(l-1):
                temp = (int(s[i]) + int(s[i+1])) % 10
                ans = ans + str(temp)
            s = ans
        if s[0] == s[1]:
            return True
        else:
            return False
        