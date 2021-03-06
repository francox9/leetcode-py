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


if __name__ == "__main__":
    import doctest
    doctest.testmod()
