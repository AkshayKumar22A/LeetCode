class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq_maps = dict()
        for c in s:
            freq_maps[c] = freq_maps.get(c,0) + 1
        
        freq_mapt = dict()
        for c in t:
            freq_mapt[c] = freq_mapt.get(c,0) + 1

        for i in freq_maps:
            if i not in freq_mapt:
                return False
            elif freq_maps[i] != freq_mapt[i]:
                return False

        return True