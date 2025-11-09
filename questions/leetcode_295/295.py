class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1
        self.size = 1

class AVLTree:
    def __init__(self):
        self.root = None
    
    def _node_height(self, node):
        # Retorna a altura do nó (0 se for None)
        return node.height if node else 0
    
    def _subtree_size(self, node):
        # Retorna o número de nós na subárvore (0 se for None)
        return node.size if node else 0
    
    def _recalculate(self, node):
        # Atualiza informações derivadas do nó: altura e tamanho da subárvore
        if node:
            node.height = 1 + max(self._node_height(node.left), self._node_height(node.right))
            node.size = 1 + self._subtree_size(node.left) + self._subtree_size(node.right)
    
    def _balance_factor(self, node):
        # Fator de balanceamento: altura(direita) - altura(esquerda)
        # positivo -> direita mais alta; negativo -> esquerda mais alta
        return self._node_height(node.right) - self._node_height(node.left) if node else 0
    
    def _rotate_right(self, root):
        # Rotação à direita (usada para reequilibrar LL / LR)
        left_child = root.left
        left_right_subtree = left_child.right
        # faz a rotação
        left_child.right = root
        root.left = left_right_subtree
        # atualiza metadados (altura e tamanho)
        self._recalculate(root)
        self._recalculate(left_child)
        return left_child
    
    def _rotate_left(self, root):
        # Rotação à esquerda (usada para reequilibrar RR / RL)
        right_child = root.right
        right_left_subtree = right_child.left
        # faz a rotação
        right_child.left = root
        root.right = right_left_subtree
        # atualiza metadados (altura e tamanho)
        self._recalculate(root)
        self._recalculate(right_child)
        return right_child
    
    def _insert(self, node, val):
        # Inserção BST padrão
        if not node:
            return TreeNode(val)

        if val < node.val:
            node.left = self._insert(node.left, val)
        else:
            # valores iguais vão para a direita na implementação atual
            node.right = self._insert(node.right, val)

        # Atualiza altura e tamanho antes de verificar balanceamento
        self._recalculate(node)
        balance = self._balance_factor(node)

        # Se desbalanceado, aplica rotações AVL adequadas
        # balance > 1 -> subárvore direita mais alta (casos RR ou RL)
        if balance > 1:
            # Se o filho direito também tem balanço >= 0 -> rotação esquerda simples (RR)
            if self._balance_factor(node.right) >= 0:
                return self._rotate_left(node)
            else:
                # Caso RL: rotação direita no filho direito, depois esquerda no nó
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

        # balance < -1 -> subárvore esquerda mais alta (casos LL ou LR)
        if balance < -1:
            # Se o filho esquerdo tem balanço <= 0 -> rotação direita simples (LL)
            if self._balance_factor(node.left) <= 0:
                return self._rotate_right(node)
            else:
                # Caso LR: rotação esquerda no filho esquerdo, depois direita no nó
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)

        return node
    
    def _kth_smallest(self, node, k):
        if not node:
            return None
        # usa o tamanho da subárvore esquerda para decidir o caminho
        left_size = self._subtree_size(node.left)
        if k == left_size + 1:
            return node.val
        elif k <= left_size:
            return self._kth_smallest(node.left, k)
        else:
            return self._kth_smallest(node.right, k - left_size - 1)
    
    def insert(self, val):
        self.root = self._insert(self.root, val)
    
    def find_kth(self, k):
        return self._kth_smallest(self.root, k)

class MedianFinder(object):

    def __init__(self):
        self.avl = AVLTree()
        self.total = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.avl.insert(num)
        self.total += 1

    def findMedian(self):
        """
        :rtype: float
        """
        if self.total % 2 == 1:
            k = (self.total + 1) // 2
            return float(self.avl.find_kth(k))
        else:
            k1 = self.total // 2
            k2 = k1 + 1
            val1 = self.avl.find_kth(k1)
            val2 = self.avl.find_kth(k2)
            return (val1 + val2) / 2.0
