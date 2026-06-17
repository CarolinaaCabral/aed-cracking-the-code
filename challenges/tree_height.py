from data_structures.node import Node


def tree_height(root: Node | None) -> int:
    if root is None:
        return -1
    altura_esquerda = tree_height(root.left)
    altura_direita = tree_height(root.right)

    return 1 + max(altura_esquerda, altura_direita)
