class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        map1 = dict()
        map2 = dict()
        count = 0
        j = 0

        for i in words1:
            map1[i] = map1.get(i, 0) + 1
        
        for j in words2:
            map2[j] = map2.get(j, 0) + 1

        for key, value in map1.items():
            j = map2.get(key, 0)
            if value == j == 1:
                count += 1
        return count