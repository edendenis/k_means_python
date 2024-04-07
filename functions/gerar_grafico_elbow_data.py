import numpy as np
import matplotlib.pyplot as plt
import pickle as pkl
from matplotlib.ticker import MaxNLocator

# Ler os objetos:
# with open("objetos.pkl", "rb") as f:
#     endereco, \
#     num_de_k_inicial, \
#     K, \
#     WSs_total_otimo_lista, \
#     banco_de_dados, \
#     distancias_otimas, \
#     populacao,\
#     ks_min_otimos = pkl.load(f)

def gerar_grafico_elbow_data(endereco,
                             num_de_k_inicial,
                             K,
                             WSs_total_otimo):

    """

    :param endereco: Endereço do banco de dados
    :param num_de_k_inicial: Número inicial do k-clusters
    :param K: Número total de k-clusters
    :param WSs_total_otimo: Within Sum total ótimo
    :return: Gráfico do  Elbow Data
    """

    # demais = 29
    # aeronaves = 25
    tamanho_da_fonte = 25

    # Atualizar parâmetros para todos os gráficos
    plt.rcParams.update({"text.usetex": True,
                        #  "text.latex.unicode": True,
                         "font.size": 12,
                         "font.family": "Book Antiqua",
                         "figure.dpi": 100,
                         "figure.figsize": (6.30, 6.30)})

    plt.close("all")

    # Normalizar os dados:
    WSs_total_otimo = WSs_total_otimo / np.max(WSs_total_otimo)

    x = np.arange(num_de_k_inicial, K + 1, 1)
    f = WSs_total_otimo

    fig  = plt.figure()
    ax = fig.add_subplot(111)

    plt.plot(x, f,
             color="b",
             marker="o",
             linestyle="-")

    f = np.concatenate(np.around(f, decimals=2))
    plt.plot(x, f)
    for xy in zip(x, f):
        ax.annotate("(%s, %s)" % xy,
                    xy=xy,
                    textcoords="data",
                    size=10)

    plt.xlim([0, K + 1])
    plt.xlabel("$ k $")
    plt.ylabel("$ WS_{Total} $ Normalizado")
    plt.title(r"\bf{Elbow Data Chart}")
    # plt.grid()

    # Maximizar a imagem
    figManager = plt.get_current_fig_manager()
    # figManager.window.showMaximized()

    ax.xaxis.set_major_locator(MaxNLocator(integer=True))

    # plt.show()  # Manter o gráfico sendo exibido sendo ao menos
    plt.tight_layout() # Ajustar o gráfico na figura


    endereco = "outputs/" + endereco + "/" + endereco + "_elbow_data_chart_" + \
        str(K) + ".jpg"
    fig.savefig(endereco, dpi=100)

# print(gerar_grafico_elbow_data(endereco,
#                              num_de_k_inicial,
#                              K,
#                              WSs_total_otimo_lista))
