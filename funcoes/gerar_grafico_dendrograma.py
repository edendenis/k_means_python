import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle as pkl

# Métodos Hierárquicos:
from scipy.cluster.hierarchy import dendrogram, linkage

# # Ler os objetos:
# [endereco,
#  banco_de_dados,
#  distancias_otimas,
#  k,
#  populacao,
#  titulo_do_eixo_x_do_dendrograma] = \
#     pkl.load(open("../pickles/objetos_den.pkl", "rb"))

def gerar_grafico_dendrograma(endereco,
                              banco_de_dados,
                              distancias_otimas,
                              k,
                              populacao,
                              titulo_do_eixo_x_do_dendrograma):

    """
    Esta subrotina gera o gráfico dendrograma.

    :param endereco: Obrigatório. str.
        Endereço do banco de dados
    :param banco_de_dados: Obrigatório. array.
        Banco de dados
    :param distancias_otimas: Obrigatório. array.
        Distâncias ótimas
    :param k: Obrigatório. int.
        Número de k-clusters
    :param populacao: Obrigatório. int.
        População/quantidade de lições
    :param titulo_do_eixo_x_do_dendrograma: Obrigatório. str.
        Título do eixo x do dendrograma sementes para exibir no eixo x do
        dendrograma.
    :return: Gráfico dendrograma.
    """

    banco_de_dados = pd.DataFrame(banco_de_dados)
    descricao_das_licoes = banco_de_dados.iloc[:, 0]

    np.set_printoptions(precision = 4,
                        suppress = True)
    # precision: Número de casas decimais
    # suppress: True, significa que a saída é float
    # e False, notação científica.
    plt.figure(figsize = (16, 10))
    # plt.style.use("seaborn-whitegrid")
    # plt.style.use("default")

    tamanho_da_letra = 16

    plt.rcParams.update({# "text.usetex": True,
                         # "text.latex.unicode": True,
                         "font.size": tamanho_da_letra,
                         "font.family": "Times New Roman",
                         "figure.dpi": 100,
                         "figure.figsize": (6.30, 6.30)})

    # Normalizar os dados
    distancias_otimas = distancias_otimas / \
                        np.max(distancias_otimas)
    distancias_otimas = pd.DataFrame(distancias_otimas)

    Y = distancias_otimas.iloc[:, 0].values

    # Usando scipy para gerar dendrogramas
    # method: método a ser utilizado na dendrogramação
        # single: mínima distância;
        # complete: máxima distância;
        # average: distância média;
        # weighted: distância ponderada;
        # centroid: distância pelo centroíde;
        # median: distância mediana;
        # ward: distância pela mínima variância de Ward
    Z = linkage(np.reshape(Y, (len(Y), 1)), method = "average")

    n = descricao_das_licoes.shape[0]
    descricao_das_licoes = list(descricao_das_licoes)

    fig = dendrogram(Z,
                     p = populacao,
                     truncate_mode = "lastp",
                     leaf_rotation = 90,
                     leaf_font_size = tamanho_da_letra,
                     labels = descricao_das_licoes,
                     orientation = "top",
                     distance_sort = "descending",
                     show_contracted = True)

    plt.title("Dendrograma Para Uma População de "
              + str(populacao) + " e $ K = $ " + str(k))
    plt.xlabel(titulo_do_eixo_x_do_dendrograma)
    plt.ylabel("Distâncias Ótimas Normalizadas")

    # plt.axhline(y = 0.5) # Inserir uma linha em y = 0.5
    # # no dendrograma
    # plt.axhline(y = 0.5) # Inserir uma linha em y = 0.5
    # # no dendrograma

    # Os comandos NÃO funcionam quando a function é
    # executada a partir do Jupyter Notebook:
    # Maximizar a imagem
    # figManager = plt.get_current_fig_manager()
    # figManager.window.showMaximized()

    # plt.show()
    plt.tight_layout()

    endereco = "saidas/dendrograma_" \
               + endereco + str(k) + ".png"
    print(endereco)
    plt.savefig(endereco)

    # Quando é gerado os dendrogramas para cada população,
    # se a função abaixo NÃO é utilizada, ocorrerá bug.
    # Além disso, a aplicação executa mais rapidamente
    # quando a mesma é utilizada!
    plt.close("all")

# print(gerar_grafico_dendrograma(endereco,
#                           banco_de_dados,
#                           distancias_otimas,
#                           k,
#                           populacao,
#                           titulo_do_eixo_x_do_dendrograma))

# REFERÊNCIA(S):

# [1] https://www.youtube.com/watch?v=JcfIeaGzF8A
# [2] https://www.youtube.com/watch?v=EUQY3hL38cw
