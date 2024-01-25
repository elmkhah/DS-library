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

    #return height of a node
    def height(self, node):
        if node is None:
            return 0
        return node.height

    #update height of a node
    def update_height(self, node):
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    #return left_height - right_height
    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    #rotate to right
    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self.update_height(y)
        self.update_height(x)

        return x

    #rotate to left
    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self.update_height(x)
        self.update_height(y)

        return y

    #balacing function 
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

    #insert to avl tree
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

    #insert key
    def insert_key(self, key):
        self.root = self.insert(self.root, key)

    #search in avl
    def search(self,key):
        return self._search(self.root,key)
        
    def _search(self,node,key):
        if not node:
            return None
        if  node.key.title==key:
         return node
        elif key<node.key.title:
          return self._search(node.left,key)
        else :return self._search(node.right,key)
    