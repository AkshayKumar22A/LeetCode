class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        first = -1
        sec = -1
        for i in range(l):
            print(nums[i])
            if nums[i] == target:
                if first == -1:
                    first = i
                sec = i
        return [first,sec]
