import itertools

# Definir um conjunto
conjunto_original = {1, 5, 14}

# Gerar o conjunto das partes
conjunto_partes = []
for i in range(len(conjunto_original) + 1):
    subsets = itertools.combinations(conjunto_original, i)
    conjunto_partes.extend(set(subset) for subset in subsets)

# Exibir o conjunto das partes
for subset in conjunto_partes:
    print(subset)
