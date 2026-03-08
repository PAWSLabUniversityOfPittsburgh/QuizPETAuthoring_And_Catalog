class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:        
    def __init__(self):
        self.head = None
        
    def add(self, new):
        new_node = Node(new)
        new_node.next = None
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node
                
    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def size(self):
        count = 0
        cur = self.head
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def contains(self, value):
        cur = self.head
        while cur is not None:
            if cur.data == value:
                return True
            cur = cur.next
        return False

    def remove_front(self):
        if self.head is None:
            return None
        value = self.head.data
        self.head = self.head.next
        return value

ll = LinkedList()
ll.add(1)
ll.add(2)
ll.add(3)
ll.print_list()
ll.size()