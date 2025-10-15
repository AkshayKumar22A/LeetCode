class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_occurence = self.find_left_occurence(nums, target)

        if left_occurence == -1:
            return [-1, -1]

        right_occurence = self.find_right_occurence(nums, target)
        return [left_occurence, right_occurence]
    
    def find_left_occurence(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        left_occurence = -1
        
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                left_occurence, end = mid, mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        
        return left_occurence

    def find_right_occurence(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        right_occurence = -1
        
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                right_occurence, start = mid, mid + 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return right_occurence