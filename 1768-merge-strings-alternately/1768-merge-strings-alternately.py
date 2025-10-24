class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        ans = ""
        i,j=0,0
        while i < l1 or j < l2:
            if i < l1:
                ans += word1[i]
            if j < l2:
                ans += word2[j]
            i+=1
            j+=1
        return ans