class Solution {
    public boolean exist(char[][] maze, String word) {
        boolean ans = false;
		for(int i=0;i<maze.length;i++)
		{
			for(int j=0;j<maze[0].length;j++)
			{
				if(word.charAt(0)==maze[i][j])
				{
					ans = findword(maze,i,j,word,0);
					if(ans==true)
					{
						return ans;
					}
				}
			}
		}
		return ans;
        
    }

    public static boolean findword(char maze[][],int currentrow,int currentcol, String word,int idx)
	{
		if(idx == word.length())
		{
			return true;
		}
		if(currentrow<0 || currentrow>=maze.length 
				|| currentcol<0 || currentcol>=maze[0].length 
					|| word.charAt(idx)!=maze[currentrow][currentcol])
		{
			return false;
		}
		maze[currentrow][currentcol] = '*';
		int R[] = {-1,1,0,0};
		int C[] = {0,0,-1,1};
		
		for(int i=0;i<R.length;i++)
		{
			boolean ans = findword(maze,currentrow+R[i],currentcol+C[i],word,idx+1);
			if(ans==true)
			{
				return true;
			}
		}
		maze[currentrow][currentcol] = word.charAt(idx);
		return false;
	}
}