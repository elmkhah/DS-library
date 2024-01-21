from book import book
class AVLNode:
    def __init__(self, key:book, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.height = 1
    
class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def update_height(self, node):
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self.update_height(y)
        self.update_height(x)

        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self.update_height(x)
        self.update_height(y)

        return y

    def balance(self, node):
        if node is None:
            return node

        self.update_height(node)

        # Left Heavy
        if self.balance_factor(node) > 1:
            # Left-Right Case
            if self.balance_factor(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # Right Heavy
        if self.balance_factor(node) < -1:
            # Right-Left Case
            if self.balance_factor(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def insert(self, root, key):
        if root is None:
            return AVLNode(key)

        if key.title < root.key.title:
            root.left = self.insert(root.left, key)
        elif key.title > root.key.title:
            root.right = self.insert(root.right, key)
        else:
            return root

        return self.balance(root)

    def insert_key(self, key):
        self.root = self.insert(self.root, key)

    def search(self,key):
        return self._search(self.root,key)
        
    def _search(self,node,key):
        if  node.key.title==key:
         return node
        elif node is None:
            return None
        elif key<node.key.title:
          return self._search(node.left,key)
        else :return self._search(node.right,key)
    