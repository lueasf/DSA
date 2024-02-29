# parenthésage valide

class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] #pile avec append et pop
        pairs = {'(': ')', '[': ']', '{': '}'}
        for b in s:
            if b in pairs:
                stack.append(b)
            elif len(stack) == 0 or pairs[stack.pop()] != b:
                return False
        return len(stack) == 0