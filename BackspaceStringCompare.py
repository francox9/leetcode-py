from types import *

# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        '''
        >>> Solution.backspaceCompare(Solution,  "a##c", "#a#c")
        True
        '''
        def removeBackspace(s: str):
            stack = []
            for ch in s:
                if ch is not '#':
                    stack.append(ch)
                elif ch is '#' and len(stack) > 0:
                    stack.pop()
            return ''.join(stack)
        return removeBackspace(S) == removeBackspace(T)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
