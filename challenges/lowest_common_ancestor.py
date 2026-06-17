from data_structures.node import Node


def lowest_common_ancestor(
    root: Node | None,
    value1: int,
    value2: int,
) -> int:
    no_atual = root

    while no_atual is not None:
        if value1 < no_atual.value and value2 < no_atual.value:
            no_atual = no_atual.left
        elif value1 > no_atual.value and value2 > no_atual.value:
            no_atual = no_atual.right
        else:
            return no_atual.value

    return -1
