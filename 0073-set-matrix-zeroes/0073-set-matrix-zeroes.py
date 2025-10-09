class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        ans = [[9 for _ in range(col)] for _ in range(row)]
        
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    for a in range(row):
                        ans[a][j] = 0
                    for b in range(col):
                        ans [i][b] = 0
                else:
                    if ans[i][j] != 0:
                        ans[i][j] = matrix[i][j]
        for i in range(row):
            for j in range(col):
                matrix[i][j] = ans[i][j]
        return matrix

        

        

        