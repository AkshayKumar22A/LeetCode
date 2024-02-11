class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> ans = new ArrayList<Integer>();
    	if(matrix.length == 0 || matrix[0].length == 0) return ans;
            
        int minR = 0;
		int maxR = matrix.length-1;
		int minC = 0;
		int maxC = matrix[0].length-1;
		int count=0;
		
		while(count < matrix.length*matrix[0].length)
		{
			for(int i=minC;i<=maxC && count < matrix.length*matrix[0].length;i++)
			{
				ans.add(matrix[minR][i]);
				count++;
			}
			minR++;
			for(int i=minR;i<=maxR && count < matrix.length*matrix[0].length;i++)
			{
				ans.add(matrix[i][maxC]);
				count++;
			}
			maxC--;
			for(int i=maxC;i>=minC && count < matrix.length*matrix[0].length;i--)
			{
				ans.add(matrix[maxR][i]);
				count++;
			}
			maxR--;
			for(int i=maxR;i>=minR && count < matrix.length*matrix[0].length;i--)
			{
				ans.add(matrix[i][minC]);
				count++;
			}
			minC++;
		}
		return ans;
    }
}