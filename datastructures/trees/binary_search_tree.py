class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Node: {self.val}'

    def __str__(self):
        return str(self.val)


class BinarySearchTree:
    """
    construct Binary Search Tree from list
    """
    def __init__(self, l=None):
        if l is None:
            l = []
        self.l = l
        self.root = None

    def build_tree(self):
        pass

    def insert(self, node_z: TreeNode):
        y = None
        x = self.root
        while x is not None:
            y = x
            if node_z.val < x.val:
                x = x.left
            else:
                x = x.right
        node_z.parent = y

        if y is None:
            self.root = node_z
        elif node_z.val < y.val:
            y.left = node_z
        else:
            y.right = node_z

    def delete(self, node_z: TreeNode):
        if node_z.left is None:
            self.transplant(node_z, node_z.right)
        elif node_z.right is None:
            self.transplant(node_z, node_z.left)
        else:
            y = BinarySearchTree.minimum(node_z.right)
            if y.parent != node_z:
                self.transplant(y, y.right)
                y.right = node_z.right
                y.right.parent = y
            self.transplant(node_z, y)
            y.left = node_z.left
            y.left.parent = y

    def transplant(self, u: TreeNode, v: TreeNode):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        if v is not None:
            v.parent = u.parent

    def search(self, node: TreeNode, val):
        """
        :param node:
        :param val: value of the node to look up
        :return: index corresponding to the node, return -1 if node does not exist
        """
        current = self.root
        while current is not None:
            if current.val == val:
                return current
            elif val > current.val:
                current = current.right
            else:
                current = current.left
        return None

    def preorder(self, node: TreeNode):
        if node is not None:
            print(str(node))
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node: TreeNode):
        if node is not None:
            self.inorder(node.left)
            print(str(node))
            self.inorder(node.right)

    def postorder(self, node: TreeNode):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(str(node))

    @staticmethod
    def maximum(node: TreeNode):
        while node.right is not None:
            node = node.right
        return node

    @staticmethod
    def minimum(node: TreeNode):
        while node.left is not None:
            node = node.left
        return node

    @staticmethod
    def parent(root: TreeNode, node: TreeNode):
        current = root
        while current is not None:
            if (current.left is not None and current.left.val == node.val) or \
                    (current.right is not None and current.right.val == node.val):
                return current
            elif node.val < current.val:
                current = current.left
            else:
                current = current.right
        return current

    def predecessor(self, root: TreeNode, node: TreeNode):
        """smallest node with val lesser than the node"""
        if node.left is not None:
            return BinarySearchTree.maximum(node.left)
        temp = self.parent(root, node)
        while temp and node.val == temp.right.val:
            node = temp
            temp = self.parent(root, temp)

        return node

    def successor(self, root, node):
        """smallest node with val greater than the node"""
        if node.right is not None:
            return BinarySearchTree.minimum(node.right)
        temp = BinarySearchTree.parent(root, node)
        while temp and node.val == temp.right.val:
            node = temp
            temp = BinarySearchTree.parent(root, temp)
        return temp

    def height(self, node: TreeNode) -> int:
        if node is None or (node.left is None and node.right is None):
            return 0
        else:
            return 1 + max(self.height(node.left), self.height(node.right))

    def get_depths(self, root: TreeNode):
        level = 0
        temp_queue = [(root, level)]
        queue = temp_queue.copy()
        while temp_queue:
            current = temp_queue.pop(0)
            if current[0].left is not None:
                temp_queue.insert(0, (current[0].left, current[1] + 1))
                queue.insert(0, (current[0].left, current[1] + 1))
            if current[0].right is not None:
                temp_queue.insert(0, (current[0].right, current[1] + 1))
                queue.insert(0, (current[0].right, current[1] + 1))

        return queue

    def print_tree(self, root: TreeNode):
        current = root
        queue = self.get_depths(current)
        queue.sort(key=lambda x: x[1])
        i = 0
        current_level = 0
        nodes_at_level = 0
        while i < len(queue):
            if i == 0:
                print('    ', end='')
            if nodes_at_level == 1:
                print('     ', end='')
            if queue[i][1] > current_level:
                print()
                current_level = queue[i][1]
                nodes_at_level = 0
            print(queue[i][0].val, end=' ')
            nodes_at_level += 1
            i += 1

        # print(queue)


if __name__ == '__main__':
    _root = TreeNode(val=15)
    _root.left = TreeNode(val=6)
    _root.right = TreeNode(val=18)
    _root.left.left = TreeNode(val=3)
    _root.left.right = TreeNode(val=7)
    _root.left.left.left = TreeNode(val=2)
    _root.left.left.right = TreeNode(val=4)
    _root.left.right.right = TreeNode(val=13)
    _root.left.right.left = TreeNode(val=9)
    bst = BinarySearchTree()
    # res = bst.predecessor(root, root.right)
    # print(str(res))
    # bst.preorder(_root)
    # print('===========')
    # bst.inorder(_root)
    # print('===========')
    # bst.postorder(_root)
    # print('\n\n\n')
    # print(bst.height(_root))
    print(bst.print_tree(_root))