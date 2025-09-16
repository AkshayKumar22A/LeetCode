class Solution:
    def isThree(self, n: int) -> bool:
        fact = []
        for i in range(1,int(sqrt(n))+1):
            if n%i == 0:
                fact.append(i)
                if i != n//i:
                    fact.append(n//i)
        ans = len(fact)
        return True if ans==3 else False
        