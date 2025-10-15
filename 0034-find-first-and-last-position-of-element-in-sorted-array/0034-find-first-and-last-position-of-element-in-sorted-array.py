class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binSearch(nums, target, True)
        right = self.binSearch(nums, target, False)
        return [left, right]

    # leftBias=[True/False], if false, res is rightBiased
    def binSearch(self, nums, target, leftBias):
        low = 0
        high = len(nums) - 1
        result = -1
        while low <= high:
            mid = (low + high) // 2
            if target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                result = mid
                if leftBias:
                    high = mid - 1
                else:
                    low = mid + 1
        return result
