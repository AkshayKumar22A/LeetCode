class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        l = len(arr)
        count = 0
        pref = [0] * (l+1)
        for i in range(l):
            pref[i+1] = pref[i] ^ arr[i]
        for i in range(l):
            for j in range(i+1,l):
                if pref[i] == pref[j+1]:
                    count+=(j-i)
        return count

        