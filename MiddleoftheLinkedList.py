# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
from types import *


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        '''
        >>> Solution.middleNode(Solution, [1, 2, 3, 4, 5, 6])
        4
        '''
        p1 = p2 = head
        while True:
            if p2.next != None:
                p2 = p2.next
            else:
                break
            p1 = p1.next
            if p2.next != None:
                p2 = p2.next
            else:
                break
        return p1.val


if __name__ == "__main__":
    import doctest
    doctest.testmod()
