class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        matrix.reverse()
        for i in range(row):
            for j in range(i,col):
                matrix[j][i],matrix[i][j] = matrix[i][j],matrix[j][i]