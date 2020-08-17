class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in '({[':
                stack.append(char)
            elif len(stack) > 0:
                if char is ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                elif char is '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                elif char is ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
            else:
                stack.append(char)
        return len(stack) == 0
