class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        ans = []
        for i in range(1,int(sqrt(area)+1)):
            if area%i == 0:
                ans.append(i)
                if i != area // i:
                    ans.append(area//i)
        ans.sort(reverse=True)
        if len(ans) == 2:
            return ans
        if len(ans) % 2 != 0:
            return ans[len(ans)//2],ans[len(ans)//2]
        else:
            return ans[(len(ans)//2)-1],ans[len(ans)//2]
        return -1
        