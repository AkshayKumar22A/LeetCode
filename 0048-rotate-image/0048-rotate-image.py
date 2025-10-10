class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        rotate = [[0 for _ in range(row)] for _ in range(col)]

        for i in range(row):
            for j in range(col):
                rotate[j][i] = matrix[i][j]

      
        for i in range(row):
            start = 0
            end = col - 1  
            while start <= end:
                rotate[i][start],rotate[i][end] = rotate[i][end],rotate[i][start]
                start+=1
                end-=1

        for i in range(row):
            for j in range(col):
                matrix[i][j] = rotate[i][j]