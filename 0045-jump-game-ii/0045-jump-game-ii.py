class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [[-1] * len(nums) for _ in range(len(nums))]
        return int(self.solve(nums,0,0,dp))
    
    def solve(self,nums,idx,step,dp):
        if idx >= len(nums)-1:
            return step
        if dp[idx][step] != -1:
            return dp[idx][step]
        
        min_step = float("inf")
        for i in range(1,nums[idx]+1):
            min_step = min(min_step,self.solve(nums,idx+i,step+1,dp))
        dp[idx][step] = min_step
        return min_step