class Tree_Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert_val(self, val):
        if self.root is None:
            self.root = Tree_Node(val)
            self.size += 1
        else:
            self._insert_helper(self.root, val)

    def _insert_helper(self, node, val):
        if val < node.val:
            if node.left is None:
                node.left = Tree_Node(val)
                self.size += 1
            else:
                self._insert_helper(node.left, val)
        elif val > node.val:
            if node.right is None:
                node.right = Tree_Node(val)
                self.size += 1
            else:
                self._insert_helper(node.right, val)

    def search(self, val):
        return self._search_helper(self.root, val)

    def _search_helper(self, node, val):
        if node is None:
            return False
        elif val == node.val:
            return True
        elif val < node.val:
            return self._search_helper(node.left, val)
        else:
            return self._search_helper(node.right, val)

    def delete_Node(self, val):
        self.root, deleted = self._delete_helper(self.root, val)
        if deleted:
            self.size -= 1

    def _delete_helper(self, node, val):
        if node is None:
            return node, False
        if val == node.val:
            if node.left is None:
                return node.right, True
            elif node.right is None:
                return node.left, True
            else:
                successor = node.right
                while successor.left:
                    successor = successor.left
                node.val = successor.val
                node.right, _ = self._delete_helper(node.right, successor.val)
        elif val < node.val:
            node.left, deleted = self._delete_helper(node.left, val)
            return node, deleted
        else:
            node.right, deleted = self._delete_helper(node.right, val)
            return node, deleted

    def size(self):
        return self.size




# Create a new BST
bst = BST()

# Insert some items
bst.insert_val(5)
bst.insert_val(3)
bst.insert_val(7)
bst.insert_val(1)
bst.insert_val(9)

# Search for an item
print(bst.search(7))  # True
print(bst.search(4))  # False

bst.delete_Node(7)
print(bst.search(7)) 

# Get the size of the tree
print(bst.size())  # 4
