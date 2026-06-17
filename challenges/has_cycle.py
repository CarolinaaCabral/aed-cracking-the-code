def has_cycle(graph: dict[str, list[str]]) -> bool:
    visitados = set()
    pilha_recursao = set()

    def dfs(no_atual):
        pilha_recursao.add(no_atual)
        for vizinho in graph.get(no_atual, []):
            if vizinho in pilha_recursao:
                return True
            if vizinho not in visitados:
                if dfs(vizinho):
                    return True
        pilha_recursao.remove(no_atual)
        visitados.add(no_atual)
        return False

    for vertice in graph:
        if vertice not in visitados:
            if dfs(vertice):
                return True
    return False
