"""Calculator

    >>> calc("+ 1 2")  # 1 + 2
    3

    >>> calc("* 2 + 1 2")  # 2 * (1 + 2)
    6

    >>> calc("+ 9 * 2 3")   # 9 + (2 * 3)
    15

Let's make sure we have non-commutative operators working:

    >>> calc("- 1 2")  # 1 - 2
    -1

    >>> calc("- 9 * 2 3")  # 9 - (2 * 3)
    3

    >>> calc("/ 6 - 4 2")  # 6 / (4 - 2)
    3
"""


def calc(s):
    """Evaluate expression."""
    chars = s.split()
    operators = {'+', '-', '*', '/'}

    def helper(num1, operator, num2):
        if operator == "+":
            return num1 + num2
        if operator == '-':
            return num1 - num2
        if operator == '*':
            return num1 * num2
        if operator == '/' and num != 0:
            return num1 / num2

    while len(chars) > 2:
        num2 = int(chars.pop())
        num1 = int(chars.pop())
        operator = chars.pop()
        num = helper(num1, operator, num2)
        chars.append(num)

    return chars[0]


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; WELL-CALCULATED! ***\n"
