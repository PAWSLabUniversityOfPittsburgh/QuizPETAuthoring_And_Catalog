class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, new):  # add to end
        new_node = DNode(new)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def print_list_forward(self):
        cur = self.head
        while cur is not None:
            print(cur.data, end=" <-> ")
            cur = cur.next
        print("None")

    def print_list_backward(self):
        cur = self.tail
        while cur is not None:
            print(cur.data, end=" <-> ")
            cur = cur.prev
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
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        return value

    def remove_back(self):
        if self.tail is None:
            return None
        value = self.tail.data
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        return value