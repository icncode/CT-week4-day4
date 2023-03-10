class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def __repr__(self):
        return f"<BST|{self.value}>"
    
    # Method to add a new node to the tree
    def insert(self, new_value):
        # if the new value is less than the current node's value
        if new_value < self.value:
            # if the current node has no left subtree
            if self.left is None:
                # Set the left subtree to be a new instance of BST
                self.left = BST(new_value)
            # if the node does have a left subtree
            else:
                # Call the insert method from the left subtree
                self.left.insert(new_value)
        else:
            # if current node has no right subtree
            if self.right is None:
                # Set the right subtree to be a new instance of BST
                self.right = BST(new_value)
            else:
                # Call the insert method from the right subtree
                self.right.insert(new_value)
                
    # Method to determine if a value is in the tree
    def contains(self, target):
        # if target is equal to node's value
        if target == self.value:
            return True
        # if target is less than the current node's value
        elif target < self.value:
            # if node's left subtree is empty (None)
            if self.left is None:
                # We know the target is not in tree because it would be here
                return False
            # if node does have left subtree
            else:
                # call the contains method on left subtree and return that value
                return self.left.contains(target)
        # if target is greater than the current node's value
        elif target > self.value:
            # if node's right subtree is empty (None)
            if self.right is None:
                # We know the target is not in tree because it would be here
                return False
            # if node does have right subtree
            else:
                # call the contains method on right subtree and return that value
                return self.right.contains(target)
            
    # Method to get the maximum value in a tree
    def get_max_value(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max_value()
        
    # Method to get the minimum value in a tree
    def get_min_value(self):
        if self.left is None:
            return self.value
        else:
            return self.left.get_min_value()
        
    # Method to remove a node from the tree
    def remove(self, value_to_remove, parent=None):
        # Move left or right to find the node to delete
        if value_to_remove < self.value:
            if self.left is not None:
                self.left.remove(value_to_remove, self)
        elif value_to_remove > self.value:
            if self.right is not None:
                self.right.remove(value_to_remove, self)
        # When we finally find the node
        else:
            # if the node to delete has both a left and right subtree - node has two children
            if self.left is not None and self.right is not None:
                # First the largest value in the left subtree and copy value to the current node
                self.value = self.left.get_max_value()
                # remote the node from which we copied
                self.left.remove(self.value, self)
            # if the left or right is None and node has no parent - node has most one child
            elif parent is None:
                # if the left side is not empty
                if self.left is not None:
                    # set root node to current node's left
                    self.value = self.left.value
                    self.left = self.left.left
                    self.right = self.left.right
                # if right side is not empty
                elif self.right is not None:
                    # Set the root node to the current node's right
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
                # if both are empty
                else:
                    self.value = None
            elif parent.left == self:
                if self.left is not None:
                    parent.left = self.left
                else:
                    parent.left = self.right
            elif parent.right == self:
                if self.left is not None:
                    parent.right = self.left
                else:
                    parent.right = self.right
                    
        
    def inorder(self,root):
        # if the node exists
        if root:
            # Call inorder on the node's left
            self.inorder(root.left)
            # print the node value
            print(root.value)
            # Call inorder on the node's right
            self.inorder(root.right)            
        
                
tree = BST(50)
tree.insert(25)
tree.insert(10)
tree.insert(75)
tree.insert(65)
tree.insert(60)
tree.insert(70)

print(tree.contains(80))

tree.inorder(tree)

tree.remove(65)