class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        ans = float("-inf")
        for num in nums:
            sum += num
            if ans < sum:
                ans = sum
            if sum < 0:
                sum = 0
        return ans