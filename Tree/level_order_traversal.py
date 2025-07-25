from queue import Queue 
# from collections import dequeue


class Node:
    def __init__ (self, val):
        self.data = val 
        self.left = None 
        self.right = None 
        
class Solution:
    def levelOrderTraversal (self, head):
        q = Queue()
        q.put(head)
        result = []
        
        while not q.empty():
            size = q.qsize()
            current_res = []
            for i in range(size):
                front = q.get()
                current_res.append(front.data)
                
                if front.left is not None:
                    q.put(front.left)
                if front.right is not None:
                    q.put(front.right)
            
            result.append(current_res)
        
        return result

if __name__ == "__main__":
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.left = Node(4)
    head.right.right = Node(5)
    
    
    follow = Solution()
    print(follow.levelOrderTraversal(head))
    
    
    
    
        