class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = len(arr) - 1
        peak = 0
        peakpos = 0
        for i in range(l):
            if arr[i] > peak:
                peak = max(arr[i],peak)
                peakpos = i
        return peakpos
        