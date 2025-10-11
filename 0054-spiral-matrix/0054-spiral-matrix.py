class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        result = []
        
        if rows == 0 or cols == 0:
            return result

        rowmin = 0
        rowmax = rows - 1 
        colmin = 0
        colmax = cols - 1
        count = 0

        while count < (rows * cols):
            i = colmin
            while i <= colmax and count < (rows * cols):
                result.append(matrix[rowmin][i])
                count+=1
                i+=1
            rowmin+=1

            j = rowmin
            while j <= rowmax and count < (rows * cols):
                result.append(matrix[j][colmax])
                count+=1
                j+=1
            colmax-=1

            k = colmax
            while k >= colmin and count < (rows*cols):
                result.append(matrix[rowmax][k])
                count+=1
                k-=1
            rowmax-=1

            l = rowmax
            while l >= rowmin and count < (rows*cols):
                result.append(matrix[l][colmin])        
                count+=1
                l-=1
            colmin+=1
        return result