class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        rowtrack = [0 for _ in range(row)]
        coltrack = [0 for _ in range(col)]

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    rowtrack[i] = -1
                    coltrack[j] = -1
        
        for a in range(row):
            for b in range(col):
                if rowtrack[a] == -1 or coltrack[b] == -1:
                    matrix[a][b] = 0