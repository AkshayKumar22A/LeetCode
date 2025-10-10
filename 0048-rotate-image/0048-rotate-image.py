class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        row = len(matrix)
        col = len(matrix[0])
        result = [[0 for _ in range(row)] for _ in range(col)]

        for i in range(row):
            for j in range(col):
                result[j][col-i-1] = matrix[i][j]

        for i in range(row):
            for j in range(col):
                matrix[i][j] = result[i][j]