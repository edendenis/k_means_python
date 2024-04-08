import numpy as np

# n = 6
# K = 4
# sementes = [[1, 4], [5, 2], [6, 1], [2, 5], [3, 4], [2, 3]]
# sementes = np.array(sementes)
# # n = Número total de elementos
# n = 6
# num_de_variaveis = 2

def sortear_sementes(n, K, sementes):
    """

    :param n: Número máximo de elementos
    :param K: Número de k-clusters
    :return: sementes_sorteadas = Array das sementes sorteadas
    """

    comprimento_do_arranjo = False
    comprimento_do_set = True
    num_de_sorteios = 0
    indices_das_sementes_sorteadas = np.zeros((K, 1), dtype=int)
    while comprimento_do_arranjo != comprimento_do_set \
            and num_de_sorteios <= n \
            or comprimento_do_set != K:
        indices_das_sementes_sorteadas = np.random.randint(0, n, K, dtype=int)
        comprimento_do_arranjo = len(indices_das_sementes_sorteadas)
        indices_das_sementes_sorteadas = set(indices_das_sementes_sorteadas)
        comprimento_do_set = len(indices_das_sementes_sorteadas)
        num_de_sorteios = num_de_sorteios + 1
    indices_das_sementes_sorteadas = \
        np.array(list(indices_das_sementes_sorteadas), dtype=int)


    sementes_sorteadas = []
    # # para todas os k-clusters fazer
    for k in range(0, K, 1):
        # formar k-medioides
        sementes_sorteadas.append(sementes[indices_das_sementes_sorteadas[k]])
    sementes_sorteadas = np.array(sementes_sorteadas, dtype=float)

    return sementes_sorteadas

# print(sortear_sementes(n, K, sementes))