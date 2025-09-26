class Solution:
    def reverseVowels(self, s: str) -> str:
        vol = {'a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U'}
        st = list(s)
        left = 0
        right = len(st)-1
        while left < right:
            if st[left] not in vol:
                left += 1
            elif st[right] not in vol:
                right -= 1
            else:
                st[left],st[right] = st[right],st[left]
                left += 1
                right -= 1
        return ''.join(st)

        