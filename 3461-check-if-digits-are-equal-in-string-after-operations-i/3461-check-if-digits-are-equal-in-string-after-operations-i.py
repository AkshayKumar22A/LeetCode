class Solution:
    def hasSameDigits(self, s: str) -> bool:
        n = len(s)
        k = n - 2
        
        digits = [ord(ch) - 48 for ch in s]

        coeffs = [1] * (n - 1)
        
        for i in range(1, k + 1):
            coeffs[i] = (coeffs[i-1] * (k - i + 1) // i)
            
        d1 = 0
        d2 = 0
        
        for i in range(n - 1): 
            coeff_mod_10 = coeffs[i] % 10
            d1 = (d1 + coeff_mod_10 * digits[i]) % 10
            d2 = (d2 + coeff_mod_10 * digits[i+1]) % 10

        return d1 == d2
        