class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        l = len(nums)
        for i in range(l+1):
            if i not in nums:
                ans = i
        return ans

        