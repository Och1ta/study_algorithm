def is_correct_bracket_seq(expression):
    left_stack = []
    for bracket in expression:
        if bracket == '(' or bracket == '[' or bracket == '{':
            left_stack.append(bracket)
        elif bracket == ")":
            if len(left_stack) == 0 or left_stack[-1] != '(':
                return False
            else:
                left_stack.pop()
        elif bracket == ']':
            if len(left_stack) == 0 or left_stack[-1] != '[':
                return False
            else:
                left_stack.pop()
        elif bracket == '}':
            if len(left_stack) == 0 or left_stack[-1] != '{':
                return False
            else:
                left_stack.pop()
    if len(left_stack) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    symbols = input()
    print(is_correct_bracket_seq(symbols))
