class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        l = len(arr)
        freq_map = dict()
        for i in range(l):
            freq_map[arr[i]] = freq_map.get(arr[i],0) + 1
        
        return len(freq_map) == len(set(freq_map.values()))