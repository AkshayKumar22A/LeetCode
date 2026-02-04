class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count = 0
        i = 0
        l1 = len(bin(start))
        l2 = len(bin(goal))
        while i <= l1 or i<= l2:
            mask = 1 << i
            #print(f"Start:{start & mask} Goal: {goal & mask}, and idc: {i}")
            if (start & mask) != (goal & mask):
                count+=1
            i+=1
        return count


        