class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        for num in nums:
            if (num-1) not in nums:
                low = 1
                while (low+num) in nums:
                    low +=1
                ans = max(low,ans)
        return ans