class Solution {
    public int countGoodSubstrings(String s) {
        int start = 0;
        int end = 0;
        int count = 0;

        while(end<s.length())
        {
            if(end-start+1==3)
            {
                if(s.charAt(start) != s.charAt(start+1) && 
                s.charAt(start+1) != s.charAt(start+2) && 
                s.charAt(start+2) != s.charAt(start))
                {
                    count++;
                }
                start++;
            }
            end++;
        }
        return count;
    }
}