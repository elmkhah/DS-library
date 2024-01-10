class AVLNode:
    def __init__(self, data=None):
        self.data = data
        self.height = 1
        self.balance_factor = 0
        self.left = None
        self.right = None


class AVLTree:
    def __init__(self):
        self.root = None

    def _height(self, node):
        if node is None:
            return 0
        return node.height

    def _update_height(self, node):
        if node is not None:
            node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _update_balance_factor(self, node):
        if node is not None:
            node.balance_factor = self._height(node.left) - self._height(node.right)

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        self._update_height(z)
        self._update_height(y)

        self._update_balance_factor(z)
        self._update_balance_factor(y)

        return y

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self._update_height(y)
        self._update_height(x)

        self._update_balance_factor(y)
        self._update_balance_factor(x)

        return x

    def _balance(self, node):
        if node is None:
            return node

        self._update_height(node)
        self._update_balance_factor(node)

        # Left Heavy
        if node.balance_factor > 1:
            # Left-Right Case
            if node.left.balance_factor < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # Right Heavy
        if node.balance_factor < -1:
            # Right-Left Case
            if node.right.balance_factor > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, root, data):
        if root is None:
            return AVLNode(data)

        if data < root.data:
            root.left = self._insert(root.left, data)
        elif data > root.data:
            root.right = self._insert(root.right, data)
        else:
            #dadeh tekrari (dar barnameh nadarim)
            return root

        return self._balance(root)


    # def inorder_traversal(self, root):
    #     if root:
    #         self.inorder_traversal(root.left)
    #         print(root.data, end=' ')
    #         self.inorder_traversal(root.right)