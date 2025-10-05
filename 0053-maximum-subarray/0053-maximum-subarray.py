class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = len(nums)
        sum = 0
        ans = float("-inf")
        for i in range(l):
            if sum < 0:
                sum = 0
            sum = sum + nums[i]
            ans = max(sum,ans)
        return ans