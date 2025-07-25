#| Complexity Type | Value                                  |
#| --------------- | -------------------------------------- |
#| **Time**        | **O(n)**                               |
#| **Space**       | **O(W)** *(maximum width of the tree)* |


from queue import Queue
class Node:
    def __init__ (self, val):
        self.data = val 
        self.left = None
        self.right = None

class Solution:
    def height (self, head):
        if head is None:
            return 0
        q = Queue()
        q.put(head)
        level = 0
        
        while not q.empty():
            size = q.qsize()
            for i in range(size):
                front = q.get()
                
                if front.left is not None:
                    q.put(front.left)
                if front.right is not None:
                    q.put(front.right)
                
            level += 1 
        return level
head = Node(1)
head.left = Node(2)
head.right = Node(3)

follow = Solution()
print(follow.height(head))
