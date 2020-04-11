from types import *


class Solution:
    def isValid(self, s: str) -> bool:
        '''
        >>> Solution.isValid(Solution, "()")
        True
        >>> Solution.isValid(Solution, "()[]{}")
        True
        >>> Solution.isValid(Solution, "(]")
        False
        '''
        stack = []
        leftParentheses = {'(', '[', '{'}
        pairs = {'()', '[]', '{}'}
        for ch in s:
            if ch in leftParentheses:
                stack.append(ch)
            else:
                if len(stack) < 1 or (stack.pop() + ch) not in pairs:
                    return False

        return len(stack) is 0


if __name__ == "__main__":
    import doctest
    doctest.testmod()
