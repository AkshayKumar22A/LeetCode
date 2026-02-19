class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq_map = dict()
        for num in nums:
            freq_map[num] = freq_map.get(num,0) + 1
        
        for i in freq_map:
            if freq_map[i] >= 2:
                return True
            
        return False

