class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        if(dividend==INT_MIN and divisor==-1):
            return INT_MAX
        if(dividend==INT_MIN and divisor==1):
            return INT_MIN

        # Determine if result is negative
        is_negative = (dividend < 0) != (divisor < 0)

        # Use absolute values for the bitwise calculation
        a, b = abs(dividend), abs(divisor)
        
        quotient = 0
        # Binary long division
        # We shift 'b' by 'i' bits to find the largest multiple of 'b' that fits in 'a'
        for i in range(31, -1, -1):
            if (b << i) <= a:
                a -= (b << i)      # Subtract the shifted divisor
                quotient |= (1 << i) # Set the corresponding bit in quotient

        # Apply the sign and clamp the result within 32-bit signed range
        result = -quotient if is_negative else quotient
        
        return result
