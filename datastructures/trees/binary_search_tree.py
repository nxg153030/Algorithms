from typing import List


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


class BinarySearchTree:
    """
    construct Binary Search Tree from list
    """
    def __init__(self, l: List = []):
        self.l = l
        self.root = None

    def build_tree(self):
        pass

    def insert(self, val):
        pass

    def delete(self, val):
        pass

    def search(self, node: TreeNode, val):
        """
        :param node:
        :param val: value of the node to look up
        :return: index corresponding to the node, return -1 if node does not exist
        """
        pass

    def preorder(self, node):
        if node is not None:
            print(str(node))
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(str(node))
            self.inorder(node.right)

    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(str(node))

    @staticmethod
    def maximum(node):
        while node.right is not None:
            node = node.right
        return node

    @staticmethod
    def minimum(node):
        while node.left is not None:
            node = node.left
        return node

    @staticmethod
    def parent(root, node):
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

    def predecessor(self, root, node):
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


if __name__ == '__main__':
    root = TreeNode(val=15)
    root.left = TreeNode(val=6)
    root.right = TreeNode(val=18)
    root.left.left = TreeNode(val=3)
    root.left.right = TreeNode(val=7)
    root.left.left.left = TreeNode(val=2)
    root.left.left.right = TreeNode(val=4)
    root.left.right.right = TreeNode(val=13)
    root.left.right.left = TreeNode(val=9)
    bst = BinarySearchTree()
    # res = bst.predecessor(root, root.right)
    # print(str(res))
    bst.preorder(root)
    print('===========')
    bst.inorder(root)
    print('===========')
    bst.postorder(root)