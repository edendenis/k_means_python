import numpy as np
import matplotlib.pyplot as plt
import pickle as pkl
from matplotlib.ticker import MaxNLocator

# # Ler os objetos:
# [endereco,
#  num_de_k_inicial,
#  K,
#  WSs_total_otimo] = \
#     pkl.load(open("../pickles/objetos_edc.pkl", "rb"))

def gerar_elbow_data_chart(endereco,
                           num_de_k_inicial,
                           K,
                           WSs_total_otimo):

    """
    Esta subrotina gera o gráfico Elbow Data Charte (EDC).

    :param endereco: Obrigatório. str.
        Endereço do banco de dados
    :param num_de_k_inicial: Obrigatório. int.
        Número inicial do k-clusters
    :param K: Obrigatório. int.
        Número total de k-clusters
    :param WSs_total_otimo: Obrigatório. float.
        Within Sum total ótimo
    :return: Elbow Data Chart
    """

    tamanho_da_fonte = 25

    # Atualizar parâmetros para todos os gráficos
    plt.rcParams.update({# "text.usetex": True,
                         # "text.latex.unicode": True,
                         "font.size": 12,
                         "font.family": "Times New Roman",
                         "figure.dpi": 100,
                         "figure.figsize": (6.30, 6.30)})

    plt.close("all")

    # Normalizar os dados:
    WSs_total_otimo = WSs_total_otimo / \
                      np.max(WSs_total_otimo)

    x = np.arange(num_de_k_inicial, K + 1, 1)
    f = WSs_total_otimo

    fig  = plt.figure()
    ax = fig.add_subplot(111)

    plt.plot(x, f,
             color = "blue",
             marker = "o",
             linestyle = "-") # Sinal de menos.

    f = np.concatenate(np.around(f, decimals = 2))
    plt.plot(x, f)
    for xy in zip(x, f):
        ax.annotate("(%s, %s)" % xy,
                    xy = xy,
                    textcoords = "data",
                    size = 10)

    plt.xlim([0, K + 1])
    plt.xlabel("$ k $")
    plt.ylabel("$ WS_{Total} $ Normalizado")
    plt.title("Elbow Data Chart (EDC)")
    # plt.grid()

    # Maximizar a imagem
    # figManager = plt.get_current_fig_manager()
    # figManager.window.showMaximized()

    ax.xaxis.set_major_locator(MaxNLocator(integer = True))

    # plt.show()  # Manter o gráfico sendo exibido sendo ao menos
    plt.tight_layout() # Ajustar o gráfico na figura

    endereco = "saidas/elbow_data_chart_" \
               + endereco + str(K) + ".jpg"
    fig.savefig(endereco, dpi = 100)

# print(gerar_elbow_data_chart(endereco,
#                              num_de_k_inicial,
#                              K,
#                              WSs_total_otimo))