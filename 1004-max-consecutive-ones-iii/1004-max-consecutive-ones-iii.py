class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = 0
        slow = 0
        fast = 0
        zero = 0
        for fast in range(len(nums)):
            if nums[fast] == 0:
                zero += 1
            if zero > k:
                if nums[slow] == 0:
                    zero -= 1
                slow += 1
            if zero <= k:
                ans = max(ans,fast-slow+1)
        return ans