class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)-1 == 0 and nums[0] == target:
            return [0,0]
        if len(nums) == 0:
            return [-1,-1]
        lb = self.lbs(nums,target)
        if lb > len(nums) - 1 or nums[lb] != target:
            return [-1,-1]
        ub = lb
        while nums[ub] == target and ub <len(nums)-1:
            if nums[ub+1] == target:
                ub+=1
            else:
                break
        return [lb,ub]
    
    def lbs(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums) - 1
        result = -1
        while start<=end:
            mid = start + (end-start) // 2
            if nums[mid] >= target:
                result = mid
                end = mid - 1
            else:
                start = mid + 1
        return result
