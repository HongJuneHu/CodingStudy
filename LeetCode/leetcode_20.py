class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        res = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        
        if len(s) % 2 == 1:
            return False
        
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            elif len(stack) == 0 and (i == ')' or i == ']' or i == '}'):
                return False
            else:
                top = stack.pop()
                if res[top] != i:
                    return False
                
        if len(stack) != 0:
            return False
        return True