class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diff = [[abs(x-i), i] for i in arr]

        result = sorted(diff, key=lambda x: (x[0], x[1]))

        return sorted([i[1] for i in result[:k]])