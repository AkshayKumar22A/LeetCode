class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        ans = 0
        l = len(nums)
        for i in range(l):
            if nums[i] == 1:
                count +=1
                ans = max(count,ans)
            else:
                count = 0
        return ans