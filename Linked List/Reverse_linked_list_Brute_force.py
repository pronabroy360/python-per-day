from collections import deque
class Node:
    def __init__ (self, data, next_node = None):
        self.data = data
        self.next = next_node
        
def reverse_linked_list(head):
    temp = head
    
    stack = deque()
    
    while temp is not None:
        stack.append(temp.data)
        temp = temp.next 
    temp = head
    
    while temp is not None:
        temp.data = stack.pop()
        
        temp = temp.next
    return head
    
def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end = " ")
        temp = temp.next 
    print()
    
# Create a linked list with
# values 1, 3, 2, and 4
head = Node(1)
head.next = Node(3)
head.next.next = Node(2)
head.next.next.next = Node(4)

# Print the original linked list
print("Original Linked List:", end=" ")
print_linked_list(head)

# Reverse the linked list
head = reverse_linked_list(head)

# Print the reversed linked list
print("Reversed Linked List:", end=" ")
print_linked_list(head)
