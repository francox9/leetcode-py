from types import *
import heapq

class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        print('asdasdfadf')
        self.stack = []
        self.heap = []

    def resetHeap(self):
        self.heap = self.stack.copy()
        heapq.heapify(self.heap)

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.resetHeap()

    def pop(self) -> None:
        self.stack.pop()
        self.resetHeap()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.heap[0]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.
