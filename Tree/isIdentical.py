class Node:
    def __init__ (self, val):
        self.data = val 
        self.left = None 
        self.right = None 

class Solution:
    def isIdentical (self, head1, head2):
        #if both of the trees are not there - if they don't even have head, they are identical
        
        if head1 is None and head2 is None:
            return True
        
        if head1 is None or head2 is None:
            return False 
        
        #check if the same nodes have the same value
        #and recursively check their left and right subtrees
        
        return (head1.data == head2.data
                and self.isIdentical(head1.left, head2.left)
                and self.isIdentical(head1.right, head2.right))

if __name__ == "__main__":
    head1 = Node(1)
    head1.left = Node(2)
    head1.right = Node(3)
    
    head2 = Node(1)
    head2.left = Node(2)
    head2.right =  Node(3)
    
    looking = Solution()
    ans = looking.isIdentical(head1, head2)
    print(ans)