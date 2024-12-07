class Solution {
    public int maximumPopulation(int[][] logs) {
        int [] people = new int[101];

        for(int i=0; i<logs.length; ++i){
            people[logs[i][0] - 1950]++;
            people[logs[i][1] - 1950]--;
        }
        int prefix = 0,maxCount = 0, date = 0;

        for(int i=0;i<101;i++) {
            prefix += people[i];
            if(prefix > maxCount) {
                maxCount = prefix;
                date = i;
            }
        }
        return date+1950;
        
    }
}