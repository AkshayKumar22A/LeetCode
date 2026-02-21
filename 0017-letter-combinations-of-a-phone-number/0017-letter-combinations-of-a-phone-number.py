class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.result = []
        
        if len(digits) == 0:
            return self.results
        
        num_map = ["","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]

        self.solve(digits,num_map,[],0)
        return self.result
    
    def solve(self,digits,num_map,subans,idx):
        if idx >= len(digits):
            self.result.append("".join(subans))
            return

        for ch in num_map[int(digits[idx])-1]:
            subans.append(ch)
            self.solve(digits,num_map,subans,idx+1)
            subans.pop()
        