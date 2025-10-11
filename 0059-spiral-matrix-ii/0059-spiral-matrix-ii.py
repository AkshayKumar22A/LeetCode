class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0 for _ in range(n)]for _ in range(n)]
        
        if n == 0:
            return result

        rowmin = 0
        rowmax = n - 1 
        colmin = 0
        colmax = n - 1
        count = 1

        while count <= (n * n):
            i = colmin
            while i <= colmax and count <= (n * n):
                result[rowmin][i] = count
                count+=1
                i+=1
            rowmin+=1

            j = rowmin
            while j <= rowmax and count <= (n * n):
                result[j][colmax] = count
                count+=1
                j+=1
            colmax-=1

            k = colmax
            while k >= colmin and count <= (n*n):
                result[rowmax][k] = count
                count+=1
                k-=1
            rowmax-=1

            l = rowmax
            while l >= rowmin and count <= (n*n):
                result[l][colmin] = count
                count+=1
                l-=1
            colmin+=1
        return result

        