class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []
        score = 0
        for i in range(len(operations)):
            if operations[i] == "+":
                score1 = result[-1]
                score2 = result[-2]
                result.append((score1+score2))
            elif operations[i] == "D":
                result.append((2*result[-1]))
            elif operations[i] == "C":
                result.pop()
            else:
                result.append(int(operations[i]))
        return sum(result)