class Solution:
    def check(self, nums: List[int]) -> bool:
        l = len(nums)
        rotations = 0
        for i in range(l):
            if nums[i] > nums[(i+1)%l]:
                rotations +=1
            if rotations > 1:
                return False
        return True

        