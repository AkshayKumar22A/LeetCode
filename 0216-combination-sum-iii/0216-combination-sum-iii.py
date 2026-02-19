class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.result = []
        idx = 1
        self.solve(k,n,0,[],idx)
        return self.result
    
    def solve(self,k,n,total,subarr,idx):
        if total == n and len(subarr) == k:
            self.result.append(subarr.copy())
            return
        if total > n or len(subarr) > k:
            return

        for i in range(idx,10):
            subarr.append(i)
            self.solve(k,n,total+i,subarr,i+1)
            subarr.pop()