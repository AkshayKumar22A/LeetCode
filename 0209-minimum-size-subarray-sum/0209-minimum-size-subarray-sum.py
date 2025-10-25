class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = len(nums)
        ans = float('inf')
        count = 0
        slow = 0
        fast = 0
        while slow < l and fast < l:
            count += nums[fast]
            while count >= target:
                ans = min(ans,fast-slow+1)
                count -= nums[slow]
                slow+=1  
            fast+=1
        return ans if ans != float('inf') else 0

                
        