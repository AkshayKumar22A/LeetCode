class Solution {
    public List<String> generateParenthesis(int n) {
        int open = 0;
		int close = 0;
		List<String> sol= new ArrayList<String>();
		Balance_Parentheses(n,"",open,close,sol);
        return sol;
    }

    public static void Balance_Parentheses(int n,String ans,int open,int close,List<String> sol)
	{

		if(open == n && close == n)
		{
			sol.add(ans);
			return;
		}
		if(open<n)
		{
			Balance_Parentheses(n,ans+"(",open+1,close,sol);
		}
		if(close < open)
		{
			Balance_Parentheses(n,ans+")",open,close+1,sol);
		}
	}
}