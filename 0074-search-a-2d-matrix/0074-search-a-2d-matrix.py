class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix) , len(matrix[0])
        low = 0
        high = rows * cols
        
        if matrix[0][0] > target or matrix[rows-1][cols-1]<target:
            return False

        while low <= high:
            mid = (low + high) // 2
            if matrix[mid // cols][mid % cols] == target:
                return True
            elif matrix[mid // cols][mid % cols] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
        