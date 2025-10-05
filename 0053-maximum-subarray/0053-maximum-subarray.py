class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = len(nums)
        sum = 0
        ans = float("-inf")
        for i in range(l):
            sum += nums[i]
            if ans < sum:
                ans = sum
            if sum < 0:
                sum = 0
        return ans