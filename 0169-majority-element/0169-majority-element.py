class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = len(nums)
        count = 0
        candidate = 0
        for i in range(l):
            if count == 0:
                candidate = nums[i]
            if nums[i] == candidate:
                count+=1
            else:
                count-=1
        return candidate