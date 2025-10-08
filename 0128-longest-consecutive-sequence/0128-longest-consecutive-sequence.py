class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        maxLength = 0
        hashMap = {}

        for i in nums:
            if i in hashMap:
                continue

            if i - 1 not in hashMap and i + 1 not in hashMap:
                hashMap[i] = 1
                if hashMap[i] > maxLength:
                    maxLength = hashMap[i]

            elif i - 1 in hashMap and i + 1 not in hashMap:
                leftEndNum = i - hashMap[i - 1]
                newLen = hashMap[leftEndNum] + 1

                hashMap[i] = newLen
                hashMap[leftEndNum] = newLen

                if newLen > maxLength:
                    maxLength = newLen

            elif i - 1 not in hashMap and i + 1 in hashMap:
                rightEndNum = i + hashMap[i + 1]
                newLen = hashMap[rightEndNum] + 1

                hashMap[i] = newLen
                hashMap[rightEndNum] = newLen

                if newLen > maxLength:
                    maxLength = newLen

            else:
                rightEndNum = i + hashMap[i + 1]
                leftEndNum = i - hashMap[i - 1]

                totalLen = hashMap[leftEndNum] + hashMap[rightEndNum] + 1

                hashMap[leftEndNum] = totalLen
                hashMap[rightEndNum] = totalLen
                hashMap[i] = totalLen

                if totalLen > maxLength:
                    maxLength = totalLen
            
        return maxLength  