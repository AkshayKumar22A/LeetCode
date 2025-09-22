class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = len(nums) // 2
        freq_map = {}
        for i in nums:
            freq_map[i] = freq_map.get(i,0) + 1
        element = 0
        count = 0
        for i in nums:
            temp = freq_map.get(i,0) 
            if count < temp:
                count = temp
                element = i
        return element