class Node: 
    def __init__ (self, value, next_node= None):
        self.value = value
        self.next = next_node
def merge_linked_list(head1, head2):
    dummy = Node(-1)
    temp = dummy
    
    while head1 is not None and head2 is not None:
        if head1.value <= head2.value:
            temp.next = head1 
            head1 = head1.next 
        else:
            temp.next = head2
            head2 = head2.next 
        temp = temp.next 
    
    if head1 is not None:
        temp.next = head1 
    else:
        temp.next = head2 
    
    return dummy.next
    

def print_linked_list (head):
    while head is not None:
        print(head.value)
        head = head.next 
    print()
    
if __name__ == "__main__":
    head1 = Node(1)
    head1.next = Node(3)
    head1.next.next = Node(5)
    
    head2 = Node(2)
    head2.next = Node(4)
    head2.next.next = Node(6)
    
    dummy = merge_linked_list(head1, head2)
    
    ans = print_linked_list(dummy)
    
    
    
    
    
    