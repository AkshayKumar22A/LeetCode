class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        for i in range(len(asteroids)):
            if asteroids[i] > 0:
                result.append(asteroids[i])
            else:
                while result and result[-1] > 0 and result[-1] < abs(asteroids[i]):
                    result.pop()
                if result and result[-1] == abs(asteroids[i]):
                    result.pop()
                elif not result or result[-1] < 0:
                    result.append(asteroids[i])

        return result