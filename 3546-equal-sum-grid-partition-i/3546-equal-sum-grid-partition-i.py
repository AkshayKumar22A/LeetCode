class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])

        # Horizontal cuts
        row_prefix = [0]
        for r in grid:
            row_prefix.append(row_prefix[-1] + sum(r))
        total_sum = row_prefix[-1]
        for i in range(1, rows):
            if row_prefix[i] == total_sum - row_prefix[i]:
                return True

        # Vertical cuts
        col_prefix = [0] * (cols + 1)
        for j in range(cols):
            column_sum = sum(grid[i][j] for i in range(rows))
            col_prefix[j + 1] = col_prefix[j] + column_sum
        total_col_sum = col_prefix[-1]
        for j in range(1, cols):
            if col_prefix[j] == total_col_sum - col_prefix[j]:
                return True

        return False