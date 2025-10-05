class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        l = len(plants)
        water = capacity
        ans = 0
        count = 0
        start = 0
        while start<l :
            if water >= plants[start]:
                print(f"water:{water}, plants:{plants[start]}")
                water -= plants[start]
                count +=1
                start+=1
            elif water < plants[start]:
                water = capacity
                count+=start*2
        return count

            
        
        