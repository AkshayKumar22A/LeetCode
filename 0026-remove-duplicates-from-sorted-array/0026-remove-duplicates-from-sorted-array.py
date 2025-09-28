class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums) - 1
        slow = 0
        fast = 0
        while(fast <= l):
            if nums[slow] == nums[fast]:
                fast+=1
            elif nums[slow] != nums[fast]:
                slow+=1
                nums[slow] = nums[fast]
        return slow+1
        