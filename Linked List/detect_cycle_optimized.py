class Node:
    def __init__ (self, value, next_node = None):
        self.value = value
        self.next = next_node

def detect_cycle_in_loop (head):
    temp = head
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next 
        fast = fast.next.next 
        if slow == fast:
            return True 
            
    return False

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

head.next.next.next.next = Node(2)

if __name__ == "__main__":
    print(detect_cycle_in_loop(head))