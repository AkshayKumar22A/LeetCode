class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        l = len(nums)
        ans = -1
        for i in range(l):
            for j in range(i+1,l):
                if nums[j] - nums[i] > ans and nums[j] - nums[i] > 0:
                    ans = nums[j] - nums[i]
        return ans