class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0: return 0
        nums.sort()

        count = 1

        n = len(nums)
        ans = 1
        for i in range(n):
            if i+1 < n:
                if nums[i] +1  == nums[i+1]:
                    count+=1
                elif nums[i] != nums[i+1]:
                    count = 1
            ans = max(ans, count)
        return ans