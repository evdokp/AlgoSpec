# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False


def balanced_brackets_1(s):
    result, position = balanced_brackets(s)
    if result:
        return 'Success'
    else:
        return str(position)

def balanced_brackets(s):
    opening_brackets_stack = []
    for i, next in enumerate(s):
        if next == '(' or next == '[' or next == '{':
            opening_brackets_stack.append(Bracket(next, i))
        if next == ')' or next == ']' or next == '}':
            if len(opening_brackets_stack) == 0:
                return False, i + 1
            top = opening_brackets_stack.pop()
            if not top.Match(next):
                return False, i + 1
    result = len(opening_brackets_stack) == 0
    if result:
        position = -1
    else:
        position = opening_brackets_stack[-1].position + 1
    return result, position

if __name__ == "__main__":
    text = sys.stdin.read()
    print(balanced_brackets_1(text))

