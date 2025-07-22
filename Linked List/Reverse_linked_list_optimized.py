class Node:
    def __init__ (self, value, next_node = None):
        self.value = value
        self.next = next_node
        
def reversed_linked_list(head):
    prev = None 
    temp = head
    
    while temp is not None:
        front = temp.next
        temp.next = prev 
        prev = temp 
        temp = front 
    return prev 

def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.value, end = " ")
        temp = temp.next 
    print()

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
print_linked_list(head)

head = reversed_linked_list(head)
print_linked_list(head)