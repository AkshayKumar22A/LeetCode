class Solution:
    def isPalindrome(self, s: str) -> bool:
        check = "".join([char for char in s if char.isalnum()])
        check = check.lower()
        print(check)
        left = 0
        right = len(check) - 1
        while left < right:
            if check[left] != check[right]:
                return False
            left += 1
            right -= 1
        return True
        