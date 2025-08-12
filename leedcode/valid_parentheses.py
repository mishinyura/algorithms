class Solution:
    def isValid(self, s: str) -> bool:
        chars = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        for ch in s:
            if ch in chars.values():
                stack.append(ch)
            else:
                if not stack or stack[-1] != chars[ch]:
                    return False
                if stack[-1] == chars[ch]:
                    stack.pop()

        return not stack


s = Solution()

print(s.isValid("["))
print(s.isValid("(("))
print(s.isValid("()[]]{}"))
print(s.isValid("()"))
print(s.isValid("(]"))
print(s.isValid("([])"))