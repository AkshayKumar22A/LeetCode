class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = len(nums)
        count = 0
        ans = 0
        for i in range(l):
            if nums[i] == 1:
                count+=1
            else:
                count=0
            ans = max(ans,count)
        return ans
        
        