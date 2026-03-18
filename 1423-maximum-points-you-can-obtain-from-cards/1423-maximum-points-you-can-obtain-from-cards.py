class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k == len(cardPoints):
            return sum(cardPoints)
        left = k-1
        leftsum = 0
        right = len(cardPoints) - 1
        rightsum = 0
        for i in range(k):
            leftsum += cardPoints[i]
        ans = leftsum
        while left >= 0 and right < len(cardPoints):
            leftsum -= cardPoints[left]
            left -= 1
            rightsum += cardPoints[right]
            right -= 1
            ans = max(ans,leftsum+rightsum)
        return ans
        