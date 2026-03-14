class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        temp = 0
        for i in range(len(asteroids)):
            if asteroids[i] > 0:
                result.append(asteroids[i])
            elif asteroids[i] < 0:
                while result and result[-1] > 0 and result[-1] <= abs(asteroids[i]):
                    temp = result.pop()
                    if temp == abs(asteroids[i]):
                        asteroids[i] = 0
                if (not result or result[-1] < 0) and asteroids[i] != 0:
                    result.append(asteroids[i])
        return result