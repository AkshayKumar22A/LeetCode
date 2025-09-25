class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        area = 0
        area = points[0][0]*(points[1][1]-points[2][1])+points[1][0]*(points[2][1]-points[0][1]) + points[2][0]*(points[0][1]-points[1][1])
        if area < 0:
            area = -area
        area = area / 2 
        print(area)
        if area != 0:
            return True
        else: return False
        