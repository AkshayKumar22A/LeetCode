class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        stack = []
        for i in range(len(arr)):
            if (arr[i]%2) != 0:
                stack.append(arr[i])
            else:
                while stack:
                    stack.pop()
            if len(stack) == 3:
                return True
        return False

