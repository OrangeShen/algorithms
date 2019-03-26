"""
Given a string containing just the characters
'(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

The brackets must close in the correct order,
"()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""


def is_valid(s: str) -> bool:
    stack = []
    dic = {")": "(",
           "}": "{",
           "]": "["}
    for char in s:
        if char in dic.values():
            stack.append(char)  # push into the stack if it's a left parenthesis
        elif char in dic:
            # if it's a right parenthesis
            if not stack or dic[char] != stack.pop():
                return False  # return False if it's not a pair with stack top or the stack is empty
    return not stack
