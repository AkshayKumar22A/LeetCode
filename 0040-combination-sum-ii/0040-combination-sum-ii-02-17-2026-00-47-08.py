class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        self.solve(candidates,target,result,target,0,[])
        return result
    
    def solve(self,candidates,target,result,total,idx,subarr):
        if total == 0:
            result.append(subarr.copy())
            return
        if total < 0:
            return
        if idx >= len(candidates):
            return
        for i in range(idx,len(candidates)):
            if i > idx and candidates[i] == candidates[i-1]:
                continue
            subarr.append(candidates[i])
            self.solve(candidates,target,result,total-candidates[i],i+1,subarr)
            subarr.pop()