class Solution {
    public List<List<Integer>> combine(int n, int k) {
        int arr[] = new int[n];
		for(int i=0;i<n;i++)
		{
			arr[i] = i+1;
		}
		List<Integer> subAns = new ArrayList<>();
		List<List<Integer>> Ans = new ArrayList<>();
		findallcombination(arr,n,k,"",0,subAns,Ans);
		return Ans;
    }

    public static void findallcombination(int arr[],int n,int k,String ans,int idx,List<Integer> subAns,List<List<Integer>> Ans)
	{
		if(k==0)
		{
			Ans.add(new ArrayList<Integer>(subAns));
			return;
		}
		
		for(int i=idx;i<arr.length;i++)
		{
			subAns.add(arr[i]);
			findallcombination(arr,n,k-1,ans+arr[i],i+1,subAns,Ans);
			subAns.remove(subAns.size()-1);
		}
	}
}