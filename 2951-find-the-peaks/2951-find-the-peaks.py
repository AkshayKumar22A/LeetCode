class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        ans = []
        l = len(mountain)
        p = 1
        while p < l-1:
            if mountain[p-1] < mountain[p] > mountain[p+1]:
                ans.append(p)
            p+=1
        return ans
