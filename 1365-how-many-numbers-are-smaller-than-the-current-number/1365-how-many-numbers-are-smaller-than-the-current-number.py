class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            count = 0
            for i in range(len(nums)):
                if nums[i] != num and nums[i] < num:
                    count += 1
            ans.append(count)
        return ans
        