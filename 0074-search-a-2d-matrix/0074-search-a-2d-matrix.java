class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int row = matrix.length;
        int col = matrix[0].length;

        boolean flag = false;

        if (matrix[0][0] > target || matrix[row - 1][col - 1] < target) {
            flag = false;
        }

        return searchMatrix_one_bs(matrix,target,row,col);
  }
    public static boolean searchMatrix_one_bs(int arr[][],int target,int row,int col)
	{
		int left = 0;
        int right = row * col - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (arr[mid / col][mid % col] == target) {
            	return true;
            	//System.out.println(flag);
            } else if (arr[mid / col][mid % col] > target) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
		return false;
	}
}