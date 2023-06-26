from collections import deque
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        if self.left is None:
            self.left = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left = self.left
            self.left = new_node

    def insert_right(self, value):
        if self.right is None:
            self.right = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right = self.right
            self.right = new_node

    def print_tree(self):
        self._print_tree_helper(self, 0)

    def _print_tree_helper(self, node, level):
        if node is not None:
            self._print_tree_helper(node.right, level + 1)
            print("    " * level + str(node.value))
            self._print_tree_helper(node.left, level + 1)

    ###Q22### Implemente uma função que retorna um array da árvore binária em pré-ordem
    def preorder_traversal(self):
        result = []
        self._preorder_traversal_helper(self, result)
        return result

    def _preorder_traversal_helper(self, node, result):
        if node is not None:
            result.append(node.value)
            self._preorder_traversal_helper(node.left, result)
            self._preorder_traversal_helper(node.right, result)


    ###Q23### Implemente uma função que retorna um array da árvore binária em in-ordem

    def inorder_traversal(self):
        result = []
        self._inorder_traversal_helper(self, result)
        return result

    def _inorder_traversal_helper(self, node, result):
        if node is not None:
            self._inorder_traversal_helper(node.left, result)
            result.append(node.value)
            self._inorder_traversal_helper(node.right, result)

    ###Q24### Implemente uma função que retorna um array da árvore binária em pós-ordem

    def postorder_traversal(self):
        result = []
        self._postorder_traversal_helper(self, result)
        return result

    def _postorder_traversal_helper(self, node, result):
        if node is not None:
            self._postorder_traversal_helper(node.left, result)
            self._postorder_traversal_helper(node.right, result)
            result.append(node.value)

    ###Q25### Implemente uma função que retorna um array da árvore binária em nível
  

    def treelevel(self):
        result = []
        queue = deque()
        queue.append(self)
        
        while queue:
            node = queue.popleft()
            result.append(node.value)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return result
    
    ###Q26### Implemente uma função que retorna a altura da árvore binária 

    def tree_height(self):
        return self._tree_height_helper(self)

    def _tree_height_helper(self, node):
        if node is None:
            return 0
        else:
            left_height = self._tree_height_helper(node.left)
            right_height = self._tree_height_helper(node.right)
            return max(left_height, right_height) + 1

    ###Q27### Implemente uma função que retorna a quantidade de elementos da árvore binária 

    def howmuch_elements(self):
        return self._howmuch_elements_helper(self)

    def _howmuch_elements_helper(self, node):
        if node is None:
            return 0
        else:
            return 1 + self._howmuch_elements_helper(node.left) + self._howmuch_elements_helper(node.right)
        
    ###Q28### Implemente uma função que retorna as folhas da árvore binária 

    def tree_leaves(self):
        return self._tree_leaves_helper(self)

    def _tree_leaves_helper(self, node):
        if node is None:
            return []

        if node.left is None and node.right is None:
            return [node.value]

        leaves = []
        if node.left is not None:
            leaves.extend(self._tree_leaves_helper(node.left))
        if node.right is not None:
            leaves.extend(self._tree_leaves_helper(node.right))

        return leaves

    ###Q29### Implemente uma função que retorna se a árvore binária é completa ou não
    def isIt_complete(self):
        def _is_complete_helper(node, index, node_count):
            if node is None:
                return True

            if index >= node_count:
                return False

            return (_is_complete_helper(node.left, 2 * index + 1, node_count) and
                    _is_complete_helper(node.right, 2 * index + 2, node_count))

        def _count_nodes(node):
            if node is None:
                return 0
            return 1 + _count_nodes(node.left) + _count_nodes(node.right)

        node_count = _count_nodes(self)
        return _is_complete_helper(self, 0, node_count)

    ###Q30### Implemente uma função que retorna se a árvore binária é estritamente binária ou não 

    def isIt_binary(self):
        return self._isIt_binary_helper(self)

    def _isIt_binary_helper(self, node):
        if node is None:
            return True

        if node.left is None and node.right is None:
            return True

        if node.left is not None and node.right is not None:
            return (
                self._isIt_binary_helper(node.left) and
                self._isIt_binary_helper(node.right)
            )

        return False

tree = BinaryTree(1)
tree.insert_left(2)
tree.insert_right(3)
tree.left.insert_left(4)
tree.left.insert_right(5)
tree.right.insert_left(6)
tree.right.insert_right(7)

tree.print_tree()


preorder_array = tree.preorder_traversal()
print(f'22) pré ordem: {preorder_array}')

inorder_array = tree.inorder_traversal()
print(f'23) in ordem: {inorder_array}')

postorder_array = tree.postorder_traversal()
print(f'24) pós ordem: {postorder_array}')

level_order_array = tree.treelevel()
print(f'25) ordem por nível: {level_order_array}')

height = tree.tree_height()
print(f'26) tamanho:{height}')

num_elements = tree.howmuch_elements()
print(f'27) numero de elementos:{num_elements}')

leaves = tree.tree_leaves()
print(f'28) folhas:{leaves}')

print(f'29) É completa? {tree.isIt_complete()}')

print(f'30) A arvore 1 é estritamente binária? {tree.isIt_binary()}')  # Saída: True

# para testar a 30, uma arvore não binaria

tree2 = BinaryTree(1)
tree2.insert_left(2)
tree2.insert_right(3)
tree2.left.insert_left(4)
tree2.left.insert_right(5)
tree2.right.insert_right(7) # observe o right seguido de right

print(f'30) A arvore 2 é estritamente binaria? {tree2.isIt_binary()}')  # Saída: False