class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
    	int row = 0, col = matrix[0].length-1;
			boolean flag = false; 
				while(row<=matrix.length-1 && col >=0)
				{
					if(matrix[row][col]==target)
					{
						return true;
					}
					else if(matrix[row][col]<target)
					{
						row++;
					}
					else if(matrix[row][col]>target)
					{
						col--;
					}
				}
			return flag;
    }
}