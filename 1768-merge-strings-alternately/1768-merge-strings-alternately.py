class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        ans = ""
        i,j=0,0
        while i <l1 and j < l2:
            ans += word1[i]
            ans += word2[j]
            i+=1
            j+=1
        while i < l1:
            ans += word1[i]
            i+=1
        while j < l2:
            ans += word2[j]
            j+=1
        return ans