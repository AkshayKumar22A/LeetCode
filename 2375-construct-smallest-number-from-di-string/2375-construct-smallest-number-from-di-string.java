class Solution {
    public String smallestNumber(String pattern) {
        int ans[] = new int [pattern.length()+1];
		Stack<Integer> st = new Stack<>(); 
		int count = 1;
		for(int i=0;i<=pattern.length();i++) {
			if(i==pattern.length() || pattern.charAt(i)=='I') {
				ans[i] = count;
				count++;
				while(!st.isEmpty()) {
					ans[st.pop()] = count;
					count++;
				}
			} else {
				st.push(i);
			}
		}
		String sol = "";
		for(int i=0;i<ans.length;i++) {
			sol += ans[i];
		}
		return sol;
    }
}