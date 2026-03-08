class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.left = None
        self.right = None

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def insert_left(self, new_node):
        if self.left == None:
            self.left = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left = self.left
            self.left = t

    def insert_right(self, new_node):
        if self.right == None:
            self.right = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right = self.right
            self.right = t

    def get_root_val(self):
        return self.key

    def set_root_val(self, val):
        self.key = val