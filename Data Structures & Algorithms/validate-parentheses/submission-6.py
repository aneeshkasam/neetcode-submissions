class Solution:
    def isValid(self, s: str) -> bool:
        result = True
        stack = []
        if len(s) % 2 != 0:
            return False

        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])

            if s[i] == ')' or s[i] == '}' or s[i] == ']':
                if len(stack) == 0:
                    result = False
                    break
                if s[i] == ')' and stack[-1] != '(':
                    result = False
                    break
                if s[i] == '}' and stack[-1] != '{':
                    result = False
                    break
                if s[i] == ']' and stack[-1] != '[':
                    result = False
                    break
                stack.pop()
            if len(stack) == 0:
                result = True
            else:
                result = False
        return result
            
                