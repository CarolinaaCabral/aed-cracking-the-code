def group_anagrams(words: list[str]) -> list[list[str]]:
    anagramas = {}

    for palavra in words:
        palavra_ordenada = "".join(sorted(palavra))

        if palavra_ordenada not in anagramas:
            anagramas[palavra_ordenada] = []

        anagramas[palavra_ordenada].append(palavra)

    return list(anagramas.values())
