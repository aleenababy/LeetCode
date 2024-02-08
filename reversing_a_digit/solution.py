

class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            reverse = str(abs(x))[::-1]
            reverse = -int(reverse)
        else:
            reverse = str(x)[::-1]
            reverse = int(reverse)

        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if reverse < INT_MIN or reverse > INT_MAX:
            return 0
        return (reverse)