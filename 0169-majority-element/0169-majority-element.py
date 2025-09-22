class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element = majority = 0
        freq_map = {}
        for i in nums:
            freq_map[i] = freq_map.get(i,0) + 1
            if freq_map[i] > majority:
                element = i
                majority = freq_map[i]
        return element