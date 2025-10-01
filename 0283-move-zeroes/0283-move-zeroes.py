class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if l < 2:
            return
        slow = 0
        fast = 1
        while fast < l:
            if nums[slow] != 0:
                slow+=1
                fast+=1
            elif nums[fast] == 0:
                fast+=1
            else:
                nums[slow],nums[fast] = nums[fast],nums[slow]
        return nums

        