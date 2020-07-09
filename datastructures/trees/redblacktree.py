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
            self.parent = None

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

    def right_rotate(self, x):
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

    def insert_fixup(self, z):
        while z.parent.color == 'RED':
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == 'RED':
                    z.parent.color = 'BLACK'
                    y.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    z = z.parent.parent
                elif z == z.parent.right:
                    z = z.parent
                    self.left_rotate(z)
                    z.parent.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    self.right_rotate(z.parent.parent)
            else:
                # same as "then" clause with right and left exchanged
                pass
        self.root.color = 'BLACK'

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u.val == u.parent.left.val:
            u.parent.left = v
        else:
            u.parent.right = v

        if v is not None:
            v.parent = u.parent

    def delete(self, z):
        if z.left is None:
            self.transplant(z, z.right)
        elif z.right is None:
            self.transplant(z, z.left)
        else:
            y = self.tree_minimum(z.right)
            if y.parent != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.lefy.parent = y

    def delete_fixup(self, x):
        while x != self.root and x.color == 'BLACK':
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 'RED':
                    w.color = 'BLACK'
                    x.parent.color = 'RED'
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == 'BLACK' and w.right.color == 'BLACK':
                    w.color = 'RED'
                    x = x.parent
                elif w.right.color == 'BLACK':
                    w.left.color = 'BLACK'
                    w.color = 'RED'
                    self.right_rotate(w)
                    w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = 'BLACK'
                    self.left_rotate(x.parent)
                    x = self.root
                else:
                    # same as then clause with right and left exchanged
                    pass
        x.color = 'BLACK'

    def tree_minimum(self, x):
        while x.left is not None:
            x = x.left
        return x

    def tree_maximum(self, x):
        while x.right is not None:
            x = x.right
        return x
