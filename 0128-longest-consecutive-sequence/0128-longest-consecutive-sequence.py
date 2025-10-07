class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l = len(nums)
        count = 0
        ans = 0
        nums.sort()
        print(l)
        if l == 0:
            return 0
        if l == 1:
            return 1
        for i in range(l-1):
            if nums[i] == nums[i+1]:
                continue
            elif nums[i] - nums[i+1] == -1:
                count+=1
            else:
                count = 0
            ans = max(ans,count)
        return ans+1