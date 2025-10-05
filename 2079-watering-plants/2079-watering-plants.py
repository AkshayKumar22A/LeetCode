class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        l = len(plants)
        water = capacity
        ans = 0
        start = 0
        while start<l :
            if water >= plants[start]:
                water -= plants[start]
                ans +=1
                start+=1
            else:
                water = capacity
                ans+=start*2
        return ans

            
        
        