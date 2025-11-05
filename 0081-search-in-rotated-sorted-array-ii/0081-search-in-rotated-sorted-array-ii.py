class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = len(nums)
        for i in range(l):
            if target == nums[i]:
                return True
        return False
        