class Solution {
    public List<String> letterCombinations(String digits) {
        List<String> ll = new ArrayList<>();
        if(digits.length()==0)
        {
            return ll;
        }
        printsol(code,digits,"",ll);
        return ll;
    }

    static String code[] = {"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};

    public static void printsol(String code[],String ques,String ans,List<String> ll)
	{
		if(ques.length()==0)
		{
			ll.add(ans);
			return;
		}
		char ch = ques.charAt(0);
		String press = code[ch-48];
		for(int i=0;i<press.length();i++)
		{
			printsol(code,ques.substring(1),ans+press.charAt(i),ll);
		}
	}
}