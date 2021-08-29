// https://leetcode.com/problems/reverse-integer

class Solution:
    def reverse(self, x: int) -> int:
        var = ""
        if x < 0:
            var = "-"
            x = x * -1
        res = list(map(int, str(x)))
        res.reverse()
        integer = int("".join(map(str, res)))

        
        if integer > 2147483647:
            return 0 
        else:
            if var == "-":
                integer = integer * -1
            return integer
        
    
    