class Node:
    def __init__ (self, val):
        self.data = val 
        self.left = None
        self.right = None 
        
class Solution:
    def isMirror (self, head1, head2):
        #if both of the nodes don't exist then it's True
        if head1 is None and head2 is None:
            return True
        
        if head1 is None or head2 is None:
            return False
        
        #if the value matches and left or right subtree matches in mirror way:
        
        return (head1.data == head2.data 
                and self.isMirror(head1.left, head2.right)
                and self.isMirror(head1.right, head2.left))

if __name__ == "__main__":
    head1 = Node(1)
    head1.left = Node(2)
    head1.right = Node(3)
    
    
    head2 = Node(1)
    head2.left = Node(3)
    head2.right = Node(2)
    
    following = Solution()
    print(following.isMirror(head1, head2))
    
    
    
    
    
    
    