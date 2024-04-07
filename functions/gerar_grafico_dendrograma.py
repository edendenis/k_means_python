# PACOTE(S): ---
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time as time
import os as os

# Métodos Hierarquicos:
import scipy
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster.hierarchy import fcluster
from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist

from pylab import rcParams
import seaborn as sb

import sklearn
from sklearn.cluster import AgglomerativeClustering
import sklearn.metrics as sm

import pickle as pkl

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

def gerar_grafico_dendrograma(endereco,
                              banco_de_dados,
                              distancias_otimas,
                              k,
                              populacao,
                              titulo_do_eixo_x_do_dendrograma):
    """
    Gera e salva um gráfico dendrograma com base nos dados fornecidos.

    :param endereco: Endereço do arquivo de entrada, incluindo o caminho completo e a extensão .xlsx.
    :param banco_de_dados: Banco de dados com as informações das entidades.
    :param distancias_otimas: Vetor de distâncias ótimas para serem normalizadas.
    :param k: Número de k-clusters para o k-means.
    :param populacao: Número de entidades na população.
    :param titulo_do_eixo_x_do_dendrograma: Título do eixo X do gráfico.
    """

    # Configuração da exibição dos gráficos
    np.set_printoptions(precision=4, suppress=True)
    plt.figure(figsize=(16, 9.9))
    tamanho_da_letra = 16
    plt.rcParams.update({
        "text.usetex": True,
        "font.size": tamanho_da_letra,
        "font.family": "Book Antiqua",
        "figure.dpi": 100,
        "figure.figsize": (6.30, 6.30)
    })

    # Normalização das distâncias
    distancias_otimas = distancias_otimas / np.max(distancias_otimas)
    Y = pd.DataFrame(distancias_otimas).loc[:, 0].values
    Z = linkage(np.reshape(Y, (len(Y), 1)), "ward")

    # Geração do dendrograma
    plt.figure()
    aeronaves = banco_de_dados.iloc[:, 0].tolist()
    dendrogram(Z,
               p=populacao,
               truncate_mode="lastp",
               leaf_rotation=90.,
               leaf_font_size=tamanho_da_letra,
               labels=aeronaves,
               orientation="top",
               distance_sort="descending",
               show_contracted=True)

    plt.title(r"\textbf{Dendrograma Para Uma População de }" + str(populacao) + r" \textbf{e} $ K = $" + str(k))
    plt.xlabel(titulo_do_eixo_x_do_dendrograma)
    plt.ylabel("Distâncias Ótimas Normalizadas")
    plt.tight_layout()

    # Processamento do nome base para remoção de segmentos numéricos no final
    nome_base = os.path.splitext(os.path.basename(endereco))[0]
    nome_base_parts = nome_base.split('_')

    # Remover a última parte se for numérica
    if nome_base_parts[-1].isdigit():
        nome_base = '_'.join(nome_base_parts[:-1])

    # Criação do diretório de saída se não existir
    pasta_base = os.path.join('outputs', nome_base)

    if not os.path.exists(pasta_base):
        os.makedirs(pasta_base)

    # Caminho completo do arquivo de saída
    endereco_completo = os.path.join(pasta_base, f"dendrograma_{nome_base}_{k}.png")
    plt.savefig(endereco_completo)
    plt.close()

# print(gerar_grafico_dendrograma(endereco,
#                               banco_de_dados,
#                               distancias_otimas,
#                               K,
#                               populacao))

# REFERÊNCIA(S): ---

# [1] https://www.youtube.com/watch?v=JcfIeaGzF8A
# [2] https://www.youtube.com/watch?v=EUQY3hL38cw

