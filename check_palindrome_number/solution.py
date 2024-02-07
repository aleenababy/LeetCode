

class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = str(x)[::-1]
        reverse = reverse
        print (reverse)
        if reverse == str(x):
            return True
        else:
            return False