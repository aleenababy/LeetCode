
# Solution 1
class Solution:
    def simpleArraySum(ar):
        sum = 0
        for i in ar:
            sum = sum + i
        return (sum)

# Solution 2
class Solution:
    def simpleArraySum(ar):
        return (sum(ar))
    
# solution 3
class Solution:
    def simpleArraySum(ar):
        if len(ar)==0:
            return 0
        return ar[0]+sum(ar[1:])