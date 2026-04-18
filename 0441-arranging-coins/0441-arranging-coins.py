class Solution:
    def arrangeCoins(self, n: int) -> int:
        ans = 0
        start = 0
        end = n
        while start <= end:
            mid = (start + end) // 2
            if (((mid + 1) * mid) // 2) <= n:
                ans = mid
                start = mid + 1
            else:
                end = mid - 1
        return ans
