class Node:
    def __init__ (self, val):
        self.data = val 
        self.left = None 
        self.right = None 

class Solution:
    def isSymmetry (self, head1, head2):
        if head1 is None and head2 is None:
            return True 
        
        if head1 is None or head2 is None:
            return False 
        
        return ( head1.data == head2.data 
                and self.isSymmetry(head1.left, head2.left)
                and self.isSymmetry(head1.right, head2.right) )
    
    def isSubtree (self, head1, head2):
        if head1 is None:
            return False 
        
        if self.isSymmetry(head1, head2):
            return True 
            
        return self.isSymmetry(head1.left, head2) or self.isSymmetry(head1.right, head2)

if __name__ == "__main__":
    root = Node(3)
    root.left = Node(2)
    root.right = Node(1)
    root.left.left = Node(11)
    root.left.right = Node(10)

    subRoot = Node(2)
    subRoot.left = Node(11)
    subRoot.right = Node(10)
    
    fol = Solution()

    print(fol.isSubtree(root, subRoot))  # Output: True
        
    
