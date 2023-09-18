class Solution {
    public int trap(int[] height) {
        return watertrap(height);
    }
    public static int watertrap(int arrf[])
	{
		int sol=0;
		int n=arrf.length;
		int left[]=new int[n];
		left[0]=arrf[0];
		for(int i=1;i< n;i++)
		{
			left[i] = Math.max(left[i-1],arrf[i]);
		}
		int right[] = new int[n]; 
		right[n-1] = arrf[n-1];
		for(int i=n-2;i>=0;i--)
		{
			right[i] = Math.max(right[i+1],arrf[i]);
		}
		for(int i=0;i<n;i++)
		{
			sol = sol+Math.min(right[i],left[i])-arrf[i];
		}
		return sol;
	}
}