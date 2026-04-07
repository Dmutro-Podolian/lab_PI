class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None
        self.height = 1


class AVLPriorityQueue:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node != None:
            return node.height
        else:
            return 0

    def balance(self, node):
        return self.height(node.left) - self.height(node.right)

    def update_height(self, node):
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    def rotate_right(self, y):
        x = y.left
        a = x.right

        x.right = y
        y.left = a

        self.update_height(y)
        self.update_height(x)

        return x

    def rotate_left(self, x):
        y = x.right
        a = y.left

        y.left = x
        x.right = a

        self.update_height(x)
        self.update_height(y)

        return y

    def insert(self, value, priority):
        self.root = self.start_insert(self.root, value, priority)

    def start_insert(self, node, value, priority):
        if not node:
            return Node(value, priority)
        if priority > node.priority:
            node.left = self.start_insert(node.left, value, priority)
        else:
            node.right = self.start_insert(node.right, value, priority)

        self.update_height(node)
        return self.is_balance(node)

    def is_balance(self, node):
        bc = self.balance(node)

        if bc > 1:
            if self.balance(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        elif bc < -1:
            if self.balance(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def extract_max(self):
        if not self.root:
            return None

        self.root, node = self.del_max(self.root)
        return node.value, node.priority

    def del_max(self, node):
        if not node.left:
            return node.right, node

        node.left, res = self.del_max(node.left)
        self.update_height(node)
        return self.is_balance(node), res

    def peek(self):
        node = self.root
        if not node:
            return None

        while node.left:
            node = node.left

        return node.value, node.priority
    
    def inorder(self):
        self.start_inorder(self.root)

    def start_inorder(self, node):
        if not node:
            return
        self.start_inorder(node.left)
        print(f"value={node.value}, priority={node.priority}")
        self.start_inorder(node.right)

