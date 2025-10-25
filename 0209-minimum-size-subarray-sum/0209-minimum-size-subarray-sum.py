class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')
        sumOfSubarray = 0
        slow = 0
        fast = 0
        while slow < len(nums) and fast < len(nums):
            sumOfSubarray += nums[fast]
            while sumOfSubarray >= target:
                ans = min(ans,fast-slow+1)
                sumOfSubarray -= nums[slow]
                slow+=1  
            fast+=1
        return ans if ans != float('inf') else 0