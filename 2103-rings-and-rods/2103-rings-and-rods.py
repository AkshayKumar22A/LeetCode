class Solution:
    def countPoints(self, rings: str) -> int:
        rods = [set() for _ in range(10)]
        for i in range(0, len(rings), 2):
            color = rings[i]
            rod = int(rings[i+1])
            rods[rod].add(color)
        return sum(1 for colors in rods if len(colors) == 3)