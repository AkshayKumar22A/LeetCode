class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for i in range(len(digits)-1,-1,-1):
            if i == len(digits)-1 and digits[i] != 9:
                digits[i] = digits[i] + 1
            elif i == len(digits)-1 and digits[i] == 9:
                digits[i] = 0
                carry = 1
            if i != len(digits)-1 and digits[i] != 9 and carry == 1:
                digits[i] = digits[i] + 1
                carry = 0
        if carry == 1:
            digits.insert(0, 1)
        return digits
        