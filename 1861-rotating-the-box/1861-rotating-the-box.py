class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        ans = [["" for _ in range(len(boxGrid))] for _ in range(len(boxGrid[0]))]
        row = len(boxGrid)
        col = len(boxGrid[0])
        print(row,col)
        for i in range(row):
            for j in range(col):
                ans[j][row-i-1] = boxGrid[i][j]

        for a in range(row):
            fast = col -1
            slow = col -1

            while fast >= 0:
                if ans[fast][a] == "#":
                    ans[fast][a] = "."
                    ans[slow][a] = "#"
                    slow -= 1
                if ans[fast][a] == "*":
                    slow = fast - 1
                fast -=1
        
        return ans


