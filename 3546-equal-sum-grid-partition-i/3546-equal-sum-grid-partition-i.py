class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        rowsum = [0] * rows
        colsum = [0] * cols
            
        for col in range(cols):
            for row in range(rows):
                rowsum[row] += grid[row][col]
                colsum[col] += grid[row][col]

        for i in range(1, rows):
            rowsum[i] = rowsum[i] + rowsum[i-1]
        total_sum = rowsum[-1]
        for i in range(0, rows):
            if rowsum[i] == total_sum - rowsum[i]:
                return True

        for i in range(1, cols):
            colsum[i] = colsum[i] + colsum[i-1]
        total_col_sum = colsum[-1]
        for j in range(0, cols):
            if colsum[j] == total_col_sum - colsum[j]:
                return True

        return False