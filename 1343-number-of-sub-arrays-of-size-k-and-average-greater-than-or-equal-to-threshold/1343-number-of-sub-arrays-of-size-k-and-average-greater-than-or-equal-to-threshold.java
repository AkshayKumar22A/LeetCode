class Solution {
    public int numOfSubarrays(int[] arr, int k, int threshold) {
        int ans = findsubarray(arr,k,threshold);
		return ans;
    }

    public static int findsubarray(int arr[],int k,int threshould)
	{
        int sum = 0;
		int count = 0;

		for(int i=0;i<k;i++)
		{
			sum = sum + arr[i];
		}

		if(sum/k >= threshould)
		{
			count++;
		}

		for(int i=k;i<arr.length;i++)
		{
			sum = sum + arr[i] - arr[i-k];
			if(sum/k >= threshould)
			{
				count++;
			}
		}
		return count;
	}
}