class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<Integer> subAnsList = new ArrayList<>();
		List<List<Integer>> FinalAns2dList = new ArrayList<>();
		coinposiblity(candidates,target,subAnsList,0,FinalAns2dList);
		return FinalAns2dList;
    }

    public static void coinposiblity(int candidates[],int target,List<Integer> subAnsList,int idx, List<List<Integer>> FinalAns2dList)
	{
		if(target == 0)
		{
			FinalAns2dList.add(new ArrayList<Integer>(subAnsList));
			return;
		}
		
		for(int i=idx;i<candidates.length;i++)
		{
			if(target >= candidates[i])
			{
				subAnsList.add(candidates[i]);
				coinposiblity(candidates,target-candidates[i],subAnsList,i,FinalAns2dList);
				subAnsList.remove(subAnsList.size()-1);
			}
		}
	}
}