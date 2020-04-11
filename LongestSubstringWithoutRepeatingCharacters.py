class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        >>> Solution.lengthOfLongestSubstring(Solution, "abcabcbb")
        3
        >>> Solution.lengthOfLongestSubstring(Solution, "bbbbb")
        1
        >>> Solution.lengthOfLongestSubstring(Solution, "pwwkew")
        3
        >>> Solution.lengthOfLongestSubstring(Solution, "dvdf")
        3
        '''
        memory = set()
        i = j = maxL = 0
        
        letters = list(s)
        l = len(letters)
        while i < l and j < l:
            if (letters[j] in memory):
                currentL = j - i
                if currentL > maxL:
                    maxL = currentL
                memory.remove(letters[i])
                i += 1
            else:
                memory.add(letters[j])
                j += 1

        return max(maxL, len(memory))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
