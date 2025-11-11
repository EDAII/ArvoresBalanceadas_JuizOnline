# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def getHeight(self, node):
        if not node:
            return 0
        if not hasattr(node, "height"):
            node.height = 1
        return node.height

    def getBalance(self, node):
        if not node:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    def rotateRight(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        return x

    def rotateLeft(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def getMinNode(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # Função principal: remove um nó e mantém a árvore balanceada
    def deleteNode(self, root, key):
        if not root:
            return root

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            successor = self.getMinNode(root.right)
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        # Corrige os quatro tipos de desequilíbrio
        # esquerda-esquerda
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rotateRight(root)
        # esquerda-direita
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)
        # direita-direita
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.rotateLeft(root)
        # direita-esquerda
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)

        return root
