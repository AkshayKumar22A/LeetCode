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
        
        for i in range(row):
            if rowtrack[i] == -1:
                for j in range(col):
                    matrix[i][j] = 0
        for i in range(col):
            if coltrack[i] == -1:
                for j in range(row):
                    matrix[j][i] = 0