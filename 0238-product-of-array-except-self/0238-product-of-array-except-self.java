class Solution {
    public int[] productExceptSelf(int[] nums) {
        return product(nums);
    }

    public static int[] product(int arrf[])
	{
		int n=arrf.length;
		int LP[] = new int [n];
		LP[0] = 1;
		for(int i=1;i<n;i++)
		{
			LP[i] = LP[i-1] * arrf[i-1];
		}
		
		int RP[] = new int [n];
		RP[n-1] = 1;
		for(int i=n-2;i>=0;i--)
		{
			RP[i] = RP[i+1] * arrf[i+1];
		}
		
		for(int i=0;i<n;i++)
		{
			LP[i] = LP[i] * RP[i];
		}
		return LP;
		
	}
}