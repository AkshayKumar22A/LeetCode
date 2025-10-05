class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = len(nums)
        sum = 0
        ans = float("-inf")
        if l < 2:
            return nums[0]
        for i in range(l):
            if sum < 0:
                sum = 0
            sum = sum + nums[i]
            ans = max(sum,ans)
        return ans