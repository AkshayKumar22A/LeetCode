class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        l = len(nums)
        a = float("-inf")
        pos = 0
        for i in range(l):
            if a < nums[i]:
                a = nums[i]
                pos = i
        for i in range(l):
            if nums[i] != a and 2*nums[i] > a:
                pos = -1
        return pos
        