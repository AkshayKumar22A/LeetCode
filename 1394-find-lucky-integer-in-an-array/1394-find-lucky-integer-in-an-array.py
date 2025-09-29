class Solution:
    def findLucky(self, arr: List[int]) -> int:
        l = len(arr)
        freq_map = dict()
        lk = -1
        for i in range(l):
            freq_map[arr[i]] = freq_map.get(arr[i],0) + 1
        for i in range(l):
            if freq_map.get(arr[i]) == arr[i]:
                if lk < arr[i]:
                    lk = arr[i]
        return lk
        