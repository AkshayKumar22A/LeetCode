class Solution {
    public List<List<String>> partition(String s) {
        List<String> ans = new ArrayList<>();
		List<List<String>> FinalAns = new ArrayList<>();
		subString(s,ans,FinalAns);
		return FinalAns;
    }

    public static void subString(String s,List<String> ans,List<List<String>> FinalAns)
	{
		if(s.length()==0)
		{
			FinalAns.add(new ArrayList<>(ans));
			return;
		}
		
		for(int i=1;i<=s.length();i++)
		{
			String sub = s.substring(0,i);
			if(isPalindrome(sub)==true)
			{
				ans.add(sub);
				subString(s.substring(i),ans,FinalAns);
				ans.remove(ans.size()-1);
			}
		}
	}

    public static boolean isPalindrome(String sub)
	{
		int start=0;
		int end=sub.length()-1;
		while(start<end)
		{
			if(sub.charAt(start)!=sub.charAt(end))
			{
				return false;
			}
			start++;
			end--;
		}
		return true;
	}
}