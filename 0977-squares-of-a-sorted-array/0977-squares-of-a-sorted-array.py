class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = len(nums)
        for i in range(0,l):
            nums[i] = nums[i] * nums[i]
            if nums[i] < 0:
                nums[i] = nums[i] + nums[i]
        nums.sort()
        return nums
        