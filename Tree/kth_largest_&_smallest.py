class Node:
    def __init__ (self, val):
        self.data = val
        self.left = None
        self.right = None 
    
class Solution:
    def reverse_inorder_traversal (self, head, counter, k, k_largest):
        
        if head is None or counter[0] >= k:
            return 
        
        
        #right traversal 
        self.reverse_inorder_traversal(head.right, counter, k, k_largest)
        
        
        counter[0] += 1
        
        #checking and updating our k_largest 
        if counter[0] == k:
            k_largest[0] = head.data 
            return 
        
        #left traversal 
        self.reverse_inorder_traversal(head.left, counter, k, k_largest)
    
    def inorder_traversal (self, head, counter1, k, k_smallest):
        
        if head is None or counter1[0] >=k:
            return 
        
        #left traversal 
        self.inorder_traversal(head.left, counter1, k, k_smallest)
        
        counter1[0] += 1
        
        #checking and updating our k_smallest value 
        if counter1[0] == k:
            k_smallest[0] = head.data 
            return
        
        #right traversal 
        self.inorder_traversal(head.right, counter1, k, k_smallest)
        


if __name__ == "__main__":
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.left = Node(4)
    head.left.right = Node(5)
    head.right.left = Node(6)
    head.right.right = Node(7)
    
    k = 3
    counter = [0]
    counter1 = [0]
    k_smallest = [0]
    k_largest = [0]
    
    fol = Solution()
    fol.reverse_inorder_traversal(head, counter, k, k_largest)
    fol.inorder_traversal(head, counter1, k, k_smallest)
    print(k_largest[0], k_smallest[0])
    
