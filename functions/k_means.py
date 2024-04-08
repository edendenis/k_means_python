import numpy as np
import functions.sortear_sementes as ss

def k_means(num_de_k_inicial, K, sementes, num_max_I):
    """

    :param num_de_k_inicial: Número de k inicial. int.
    :param K: Número total de k-clusters. int
    :param sementes: Sementes do BIG Data. float.
    :param num_max_I: Número máximo de iterações. int.
    
    :return: Medioides ótimos, posição mais próxima do 
    medioide ótimo e WSs total ótimos
    """

    # I = Iteração
    I = 0  # Iteração inicial

    # n = Número total de elementos
    n = sementes.shape[0]

    # num_de_variaveis = Número de variáveis
    num_de_variaveis = sementes.shape[1]

    # O medioide deve ser um novo arranjo
    # medioides = np.zeros((K, num_de_variaveis), dtype=float)

    # o medioide anterior deve ser um novo arranjo
    medioides_anteriores = np.ones((K, num_de_variaveis), dtype=float)

    # num_de_elementos_na_soma = Número de elementos na soma para calcular
    # os novos medioides
    num_de_elementos_na_soma = np.zeros((K, 1), dtype=int)

    # a distância deve ser um novo arranjo
    distancias = np.zeros((n, K), dtype=float)

    # soma_medioides = np.zeros((K, 1, num_de_variaveis), dtype = float)
    soma_medioides = np.zeros((K, num_de_variaveis), dtype=float)

    # ks_min = Arranjo de k-clusters que as sementes estão mais próximas
    ks_min = np.zeros((n, 1), dtype=int)

    # o Within Sum anterior deve ser um novo arranjo
    # WSs_anteriores = np.zeros((K, 1), dtype = float)
    # o Within Sum deve ser um novo arranjo
    WSs = np.ones((K, 1), dtype=float)

    # o Within Sum total deve ser um novo arranjo
    # WStotals = np.ones((K, 1), dtype = float)
    WS_total = True

    # O Within Sum total ótimo deve ser um novo arranjo
    WS_total_otimo = np.inf

    # Distancias ótimas deve ser um novo arranjo
    distancias_otimas = np.zeros((n, 1), dtype=float)

    # enquanto WS total for diferente do WS total anterior fazer
    while I <= num_max_I:

        # para todas os k-clusters fazer
        # sortear semente k
        # formar k-medioides
        # for k in range(0, K, 1):
        medioides = ss.sortear_sementes(n, K, sementes)

        while np.array_equal(medioides, medioides_anteriores) == False and I <= num_max_I:

            num_de_elementos_na_soma[:] = 0
            sortear_novamente = False
            while num_de_elementos_na_soma.any() == 0:

                if num_de_elementos_na_soma.any() == 0 \
                        and sortear_novamente == True:
                    # for k in range(0, K, 1):
                    medioides = ss.sortear_sementes(n, K, sementes)

                distancias[:] = 0 # Zerar todos os elementos do array
                soma_medioides[:] = 0
                num_de_elementos_na_soma[:] = 0
                # calcular a distância entre o elemento e o medioide
                for i in range(0, n, 1):
                    # para todos os $ k $-clusters
                    for k in range(0, K, 1):
                        distancias[i, k] = \
                            np.linalg.norm(sementes[i] - medioides[k])

                    # comparar a distância entre o elemento do BIG Data e o medioide
                    # associar esta distância ao medioide de menor distância
                    # k_min = Índice do medioide m_k de menor distância

                    k_min = distancias.tolist()[i].index(min(distancias[i, :]))
                    # print(i) # Adicionado

                    ks_min[i, 0] = k_min

                    soma_medioides[k_min] = soma_medioides[k_min] + sementes[i]
                    num_de_elementos_na_soma[k_min] = \
                        num_de_elementos_na_soma[k_min] + 1

                if num_de_elementos_na_soma.any() == 0:
                    sortear_novamente = True

            # recalcular (média dos pontos aglutinados), novos medioides
            medioides_anteriores = medioides.copy()
            # para todos os $ k $-clusters
            for k in range(0, K, 1):
                medioides[k] = soma_medioides[k] / num_de_elementos_na_soma[k]

            distancias[:] = 0 # Zerar todos os elementos do array
            WSs[:] = 0
            # calcular a distância entre o elemento e o novo medioide
            for i in range(0, n, 1):
                # para todos os $ k $-clusters
                for k in range(0, K, 1):
                    distancias[i, k] = np.linalg.norm(sementes[i] - medioides[k])

                # comparar a distância entre o elemento do BIG Data e o novo medioide
                # associar esta distância ao novo medioide de menor distância
                # k_min = Índice do medioide m_k de menor distância
                k_min = distancias.tolist()[i].index(min(distancias[i, :]))

                ks_min[i, 0] = k_min

                WSs[k_min] = WSs[k_min] + distancias[i, k_min]

            # Calcular WS
            ks_min_anteriores = ks_min
            WS_total_anteriores = WS_total
            WS_total = sum(WSs)

            # Comparar WS_total com WS_otimo
            if WS_total <= WS_total_otimo:
                ks_min_otimos = ks_min_anteriores.copy()
                medioides_otimos = medioides.copy()
                WS_total_otimo = WS_total
            elif WS_total > WS_total_otimo:
                ks_min_otimos = ks_min_otimos.copy()
                medioides_otimos = medioides_otimos.copy()
                WS_total_otimo = WS_total_otimo

            I = I + 1

    # calcular a distância entre o elemento e o novo medioide
    for i in range(0, n, 1):
        # para todos os $ k $-clusters
        for k in range(0, K, 1):
            distancias_otimas[i, 0] = \
                np.linalg.norm(sementes[i] - medioides_otimos[k, 0])

    return distancias_otimas, medioides_otimos, \
           ks_min_otimos, WS_total_otimo
