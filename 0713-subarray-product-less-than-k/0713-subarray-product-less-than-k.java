class Solution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        return Count_of_SubArray(nums,k);
    }

    public static int Count_of_SubArray(int arr[],int k)
	{
		int start = 0;
		int end = 0;
		int prod = 1;
		int sol = 0;
		
		while(end<arr.length)
		{
			//Growing
			prod = prod * arr[end];
			
			//Shrinking
			while(prod >= k && start <= end)
			{
				prod = prod / arr[start];
				start++;
			}
			
			//Answer Calculation
			sol = sol + (end - start +1);
			end++;
		}
		return sol;
	}
}