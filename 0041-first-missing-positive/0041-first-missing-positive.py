class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        l = max(nums)
        freq_map = dict()
        for i in range(len(nums)):
            freq_map[nums[i]] = freq_map.get(nums[i],0)+1
        for i in range(1,l+2):
            if i not in freq_map:
                return i
        return 1
        