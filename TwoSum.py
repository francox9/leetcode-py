from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        i = 0
        j = 0
        for i in range(len(nums)):
            dictionary[nums[i]] = i
        i = 0
        while i < len(nums):
            j = dictionary.get(target - nums[i])
            if (j != None and i != j):
                break
            i += 1
        
        return [i, j]


s = Solution()

print(s.twoSum([3, 3], 6))
