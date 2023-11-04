class Solution {
    public List<Integer> lexicalOrder(int n) {
        List<Integer> sol = new ArrayList<>();
        printlexico(0,n,sol);
        return sol;
    }

    public static void printlexico(int current,int n,List<Integer> sol)
    {
        if(current>n)
        {
            return;
        }
        
        if(current!=0)
        {
            sol.add(current);
        }

        int i=0;
        if(current == 0)
        {
            i=1;
        }
        while(i<=9)
        {
            printlexico(current*10+i,n,sol);
            i++;
        }
    }
}