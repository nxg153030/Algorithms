class RedBlackTree:
    def __init__(self):
        self.root = None
        self.nil = None

    class Node:
        def __init__(self, val, color):
            self.val = val
            self.color = color
            self.left = None
            self.right = None

    def left_rotate(self, node_x):
        node_y = node_x.right
        node_x.right = node_y.left

        if node_y.left != self.nil:
            node_y.left.parent = node_x
        node_y.parent = node_x.parent

        if node_x.parent == self.nil:
            self.root = node_y
        elif node_x == node_x.parent.left:
            node_x.parent.left = node_y
        else:
            node_x.parent.right = node_y
        node_y.left = node_x
        node_x.parent = node_y

    def right_rotate(self):
        pass

    def insert(self, node_z):
        node_y = self.nil
        node_x = self.root
        while node_x != self.nil:
            node_y = node_x
            if node_z.key < node_x.key:
                node_x = node_x.left
            else:
                node_x = node_x.right
        node_z.parent = node_y
        if node_y == self.nil:
            self.root = node_z
        elif node_z.key < node_y.key:
            node_y.left = node_z
        else:
            node_y.right = node_z
        node_z.left = self.nil
        node_z.right = self.nil
        node_z.color = 'red'
        self.insert_fixup(node_z)

    def insert_fixup(self, node_z):
        pass

    def transplant(self):
        pass

    def delete(self):
        pass

    def delete_fixup(self):
        pass