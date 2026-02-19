class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        self.solve(nums, 0, [], result)
        return result

    def solve(self, nums, idx, subset, result):
        if idx >= len(nums):
            if subset not in result:
                result.append(subset.copy())
            return
    
        subset.append(nums[idx])
        self.solve(nums, idx + 1, subset, result)
        subset.pop()
        self.solve(nums, idx + 1, subset, result)
        