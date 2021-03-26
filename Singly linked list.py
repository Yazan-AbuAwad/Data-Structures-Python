class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
    
    def view_list(self):
        current = self.head
        while current:
            if current.next:
                print(current.data, end='-->')
            else:
                print(current.data, end='\n')
            current = current.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        #iterate list to reach the end of it
        pointer = self.head
        while pointer.next: #if it is not none
            pointer = pointer.next
        
        pointer.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def add_after(self,prev,data):
        if not prev:
            print("No previous node!")
            return
        
        new_node = Node(data)
        new_node.next = prev.next
        prev.next = new_node

    def delete_node(self, key):
        current = self.head
        # deleting the head
        if current and current.data == key: 
            self.head = current.next
            current = None
            return
        
        #deleting other nodes first look for node and keep track of previous node
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        
        if not current:
            return
        prev.next = current.next
        current = None

    def list_length(self,node): #node is self.head
        if node is None:
            return 0 
        return 1 + self.list_length(node.next)
        

ll = linkedlist()
ll.append("A")
ll.append("B") 
ll.append('C')
ll.append('D')

ll.view_list()
