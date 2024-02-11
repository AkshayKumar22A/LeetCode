class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
        int arr[] = new int [9];
		for(int i=0;i<9;i++)
		{
			arr[i] = i+1;
		}
		List<Integer> subAns = new ArrayList<>();
		List<List<Integer>> Ans2D = new ArrayList<>();
		sumcombination(arr,k,n,0,"",subAns,Ans2D);
		return Ans2D;
    }

    public static void sumcombination(int arr[],int k, int n,int idx,String ans,List<Integer> subAns,List<List<Integer>> Ans2D) 
	{
		if(k==0 && n==0)
		{
			Ans2D.add(new ArrayList<>(subAns));
			return;
		}
		for(int i=idx;i<arr.length;i++)
		{
			subAns.add(arr[i]);
			sumcombination(arr,k-1,n-arr[i],i+1,ans+arr[i],subAns,Ans2D);
			subAns.remove(subAns.size()-1);
		}
	}
}