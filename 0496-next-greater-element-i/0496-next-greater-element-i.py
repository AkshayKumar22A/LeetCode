class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for i in range(len(nums1)):
            ans = -1
            temp = -1
            for j in range(0,len(nums2)):
                if nums1[i] == nums2[j]:
                    temp = nums1[i]
                if temp != -1 and temp < nums2[j]:
                    ans = nums2[j]
                    break
            result.append(ans)
        return result