class Solution:
    def myAtoi(self, s: str) -> int:
            INT_MIN, INT_MAX = -2**31, 2**31 - 1
    
            # Step 1: Ignore leading whitespace
            s = s.lstrip()
            
            # Step 2: Check for sign
            sign = 1
            if s and (s[0] == '-' or s[0] == '+'):
                sign = -1 if s[0] == '-' else 1
                s = s[1:]
            
            # Step 3: Read digits until non-digit or end of string
            result = 0
            for char in s:
                if not char.isdigit():
                    break
                result = result * 10 + int(char)
            
            # Step 4: Apply sign
            result *= sign
            
            # Step 5: Clamp to 32-bit signed integer range
            result = max(INT_MIN, min(INT_MAX, result))
            
            return result