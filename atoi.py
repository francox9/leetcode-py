import re

class Solution:
    def myAtoi(self, str: str) -> int:
        '''
        >>> Solution.myAtoi(Solution, "42")
        42
        >>> Solution.myAtoi(Solution, "   -42")
        -42
        >>> Solution.myAtoi(Solution,  "4193 with words")
        4193
        >>> Solution.myAtoi(Solution,  "words and 987")
        0
        >>> Solution.myAtoi(Solution,  "-91283472332")
        -2147483648
        '''
        try:
            numString, *rest = re.findall("^[+-]?\d+", str.lstrip())
            num = int(numString)
            # num
            MAX = 1 << 31
            if num > MAX - 1:
                return MAX - 1
            elif num + MAX < 0:
                return -MAX
            else:
                return num

        except:
            return 0
        


if __name__ == "__main__":
    import doctest
    doctest.testmod()
