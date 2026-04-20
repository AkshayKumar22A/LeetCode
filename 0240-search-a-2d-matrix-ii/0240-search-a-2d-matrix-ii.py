class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows):
            if matrix[i][0] > target:
                continue
            if matrix[i][-1] < target:
                continue
            low = 0
            high = cols - 1
            while low <= high:
                mid = (low + high) // 2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
        return False
        