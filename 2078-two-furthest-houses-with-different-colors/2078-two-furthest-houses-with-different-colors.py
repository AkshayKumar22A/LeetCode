class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        dist = [-1] * len(colors)
        for i in range(len(colors)):
            for j in range(i,len(colors)):
                if colors[i] != colors[j]:
                    dist[i] = abs(i - j)
        return max(dist)