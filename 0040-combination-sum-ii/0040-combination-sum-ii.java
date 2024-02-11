class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
		Arrays.sort(candidates);
		List<Integer> subAns = new ArrayList<>();
		List<List<Integer>> AnsList = new ArrayList<>();
		subCombination(candidates,target,0,"",subAns,AnsList);
		return AnsList;
    }

    public static void subCombination(int arr[],int target,int idx,String Ans,List<Integer> subAns, List<List<Integer>> AnsList)
	{
		if(target == 0)
		{
			AnsList.add(new ArrayList<>(subAns));
			return;
		}
		
		for(int i=idx;i<arr.length;i++)
		{
			if(i>idx && arr[i] == arr[i-1])
			{
				continue;
			}
			if(arr[i] > target)
			{
				break;
			}
			subAns.add(arr[i]);
			subCombination(arr,target-arr[i],i+1,Ans+arr[i],subAns,AnsList);
			subAns.remove(subAns.size()-1);
		}
	}
}