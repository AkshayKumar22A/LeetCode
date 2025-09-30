class Solution:
    def countPoints(self, rings: str) -> int:
        count = 0
        red = [0] * 10
        blue = [0] * 10
        green = [0] * 10
        l = len(rings)
        for i in range(0,l,2):
            if rings[i] == 'R':
                red[int(rings[i+1])] +=1
            elif rings[i] == 'G':
                green[int(rings[i+1])] +=1
            elif rings[i] == 'B':
                blue[int(rings[i+1])] +=1
        for i in range(0,10):
            if blue[i] > 0 and red[i] > 0 and green[i] > 0:
                count+=1
        return count


        