class Node( value, next_node = None):
    self.value = value
    self.next = next_node

def detectCycle(head):
    temp = head
    Node_set = set()
    
    while temp is not None:
            
        if temp in Node_set:
            return True
        
        
        Node_set.append(temp)
        temp = temp.next 
    return False

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(2)