class Solution:
    def countPoints(self, rings: str) -> int:
        count = 0
        tracker = [''] * 10
        l = len(rings)
        for i in range(1,l,2):
            if rings[i-1] == "B":
                tracker[int(rings[i])] += "B"
            if rings[i-1] == "G":
                tracker[int(rings[i])] += "G"
            if rings[i-1] == "R":
                tracker[int(rings[i])] += "R"
        for i in range(0,10):
            if "R" in tracker[i] and "G" in tracker[i] and "B" in tracker[i]:
                count+=1
        return count


        