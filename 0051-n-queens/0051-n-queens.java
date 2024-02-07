class Solution {
    public List<List<String>> solveNQueens(int n) {
        char[][] board = new char[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                board[i][j] = '.';
        List<List<String>> ans = new ArrayList<> ();
        queen(0, board, ans,n);
        return ans;
    }

    public static void queen(int row, char[][] board, List<List<String>>ans,int tq) {
        if (tq==0) {
            ans.add(construct(board));
            return;
        }

        for (int col = 0; col < board.length; col++) {
            if (validate(board, row, col)) {
                board[row][col] = 'Q';
                queen(row+1, board, ans,tq-1);
                board[row][col] = '.';
            }
        }
    }

    public static boolean validate(char[][] board, int row, int col) 
    {
        //Up
        for(int i=row;i>=0;i--)
		{
			if(board[i][col]=='Q')
			{
				return false;
			}
		}
        //Left Diagonal
        for(int i=row,j=col;i>=0 && j>=0;i--,j--)
		{
			if(board[i][j]=='Q')
			{
				return false;
			}	
		}
		//Right Diagonal
		for(int i=row,j=col;i>=0 && j<board.length;i--,j++)
		{
			if(board[i][j]=='Q')
			{
				return false;
			}			
		}
        return true;
    }

    public static List<String> construct(char[][] board) {
        List<String> ans = new ArrayList<String>();
        for (int i = 0; i < board.length; i++) {
            String s = new String(board[i]);
            ans.add(s);
        }
        return ans;
    }
}