class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []
        score = 0
        for i in range(len(operations)):
            print(result)
            if not(operations[i] == "+" or operations[i] == "D" or operations[i] == "C"):
                result.append(int(operations[i]))
            elif operations[i] == "+":
                score1 = result[-1]
                score2 = result[-2]
                result.append((score1+score2))
            elif operations[i] == "D":
                result.append((2*result[-1]))
            elif operations[i] == "C":
                result.pop()
        return sum(result)