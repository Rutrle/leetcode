
def is_valid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    open_parentheses = {'(', '[', '{'}
    close_parentheses = {')': '(', ']': '[', '}': '{'}
    for letter in s:
        if letter in open_parentheses:
            stack.append(letter)
        elif not stack:
            return False
        else:
            current_char = stack.pop()
            if close_parentheses[letter] != current_char:
                return False

    if len(stack) == 0:
        return True

    return False


print(is_valid('[]{}[][][[]]'))


print(is_valid('[]{}[()][)][[]]'))
