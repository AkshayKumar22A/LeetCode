class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        
        total_sum = sum(sum(row) for row in grid)
    
        if total_sum % 2 != 0:
            return False

        target_sum = total_sum // 2
        
        # Check for Horizontal Cuts (Row-wise Prefix Sum)
        current_sum = 0
        for i in range(rows - 1):
            current_sum += sum(grid[i])
            if current_sum == target_sum:
                return True
        
        # Check for Vertical Cuts (Column-wise Summation)
        current_sum = 0
        for j in range(cols - 1):
            column_sum = 0
            for i in range(m):
                column_sum += grid[i][j]
            current_sum += column_sum
            if current_sum == target_sum:
                return True

        return False   