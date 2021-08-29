// https://leetcode.com/problems/valid-parentheses

class Solution(object):
    def isValid(self, s):
        dict = {
            "[": "]",
            "{": "}",
            "(": ")"
        }
        opens = ['[', '{', '(']
        closed = [']', '}', ')']
        stack = []
        lst = list(s)
        if len(s) < 2:
            return False
        if lst[0] in closed or lst[-1] in opens:
            return False
        
        for i in range(len(lst)):
            if lst[i] in opens:
                stack.append(lst[i])
            else:
                if len(stack) != 0:
                    k = stack.pop()
                    if dict[k] != lst[i]:
                        return False
                else:
                    return False
                
        if len(stack) == 0:
            return True
        else:
            return False

                
        