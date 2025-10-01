class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        total = l*(l+1)//2
        nums_sum = sum(nums)
        return total - nums_sum

        