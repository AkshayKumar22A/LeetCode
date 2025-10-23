class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        totalSum = 0
        s=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                totalSum += grid[i][j]
        
        for i in range(len(grid)):
            if i==len(grid)-1:
                break
            for j in range(len(grid[0])):
                s+=grid[i][j]
            reqSum = totalSum-s
            if reqSum==s:
                return True
        
        s=0
        for i in range(len(grid[0])):
            if i ==len(grid[0])-1:
                break
            for j in range(len(grid)):
                s+=grid[j][i]
            reqSum = totalSum-s
            if(reqSum==s):
                return True
        return False