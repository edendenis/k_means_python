# PACOTE(S): ---
import numpy as np
import pandas as pd
import time as time
import os as os

# Formatação de plotagem:
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (16, 9)  # Tamanho da figura
plt.rcParams['font.family'] = 'serif'  # Escolha o tipo de fonte
plt.rcParams['font.size'] = 12  # Tamanho da fonte (NÂO especificada)
plt.rcParams["axes.labelsize"] = 14  # Tamanho da fonte do rótulo dos eixos
plt.rcParams["xtick.labelsize"] = 12  # Tamanho da fonte do eixo x
plt.rcParams["ytick.labelsize"] = 12  # Tamanho da fonte do eixo y
plt.rcParams["legend.fontsize"] = 12  # Tamanho da fonte da legenda
plt.rcParams['lines.linewidth'] = 2  # Espessura da(s) linha(s) plotadas
plt.rcParams['axes.grid'] = True  # Ativar a grade no gráfico
plt.rcParams['grid.alpha'] = 0.5  # Transparência da linha da grade
plt.rcParams["figure.dpi"] = 200  # Densidade mínima de pixels

# Aproveite o melhor do ggplot e do seaborn
plt.style.use("ggplot")
plt.style.use("seaborn-deep")

plt.rcParams["figure.autolayout"] = True

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
                              num_de_k_inicial,
                              k,
                              populacao,
                              titulo_do_eixo_x_do_dendrograma,
                              k_large,
                              num_max_I):
    """
    Gera e salva um gráfico dendrograma com base nos dados fornecidos.

    :param endereco: Endereço do arquivo de entrada, incluindo o caminho completo e a extensão .xlsx.
    :param banco_de_dados: Banco de dados com as informações das entidades.
    :param distancias_otimas: Vetor de distâncias ótimas para serem normalizadas.
    :param k: Número de k-clusters para o k-means.
    :param populacao: Número de entidades na população.
    :param titulo_do_eixo_x_do_dendrograma: Título do eixo X do gráfico.
    :param k_large: Número total de cluster. int. 
    :param num_max_I: Número máximo de iterações. int.

    :return None
    """
    
    # Normalização das distâncias
    distancias_otimas = distancias_otimas / np.max(distancias_otimas)
    Y = pd.DataFrame(distancias_otimas).loc[:, 0].values
    Z = linkage(np.reshape(Y, (len(Y), 1)), "ward")

    # Configuração da exibição dos gráficos
    np.set_printoptions(precision=4, suppress=True)
    [figure, subchart] = plt.subplots(nrows=1, ncols=1,
                                      sharex=True, sharey=False,
                                      figsize=(24, 11))

    # Geração do dendrograma
    produtos = banco_de_dados.iloc[:, 0].tolist()
    dendrogram(Z,
               p=populacao,
               truncate_mode="lastp",
               leaf_rotation=90.,
               # leaf_font_size=tamanho_da_letra,
               labels=produtos,
               orientation="top",
               distance_sort="descending",
               show_contracted=True,
               ax=subchart)  # Usar 'ax=subchart' para desenhar no eixo especificado
    
    # Configuração dos títulos e labels usando o objeto 'subchart'
    subchart.set_title(r"Dendrograma Para Uma População máxima de " + \
                       str(populacao) + r" e $ K = $" + str(k) + " clusteres")
    subchart.set_xlabel(titulo_do_eixo_x_do_dendrograma)
    subchart.set_ylabel("Distâncias Ótimas Normalizadas")
    figure.tight_layout()  # Use 'figure' em vez de 'plt' para aplicar tight_layout na figura inteira

    # Encontrar o caminho para a pasta 'outputs' dentro de 'k_means'
    caminho_base = os.path.dirname(endereco)  # Sobe um nível para 'k_means'
    pasta_outputs = os.path.join(caminho_base, 'outputs')

    # Processamento do nome base
    nome_base = os.path.splitext(os.path.basename(endereco))[0].replace("__", "_") + \
        f"_de_{num_de_k_inicial}_ate_{k_large}_clusters_com_{num_max_I}_iteracoes"
    nome_base_parts = nome_base.split('_')

    # Remover a última parte se for numérica
    if nome_base_parts[-1].isdigit():
        nome_base = '_'.join(nome_base_parts[:-1])

    # Criação do diretório de saída se não existir
    pasta_base = os.path.join(pasta_outputs, nome_base)
    pasta_base = pasta_base.replace("__", "_")
    os.makedirs(pasta_base, exist_ok=True)  # Cria o diretório se não existir

    # Caminho completo do arquivo de saída
    endereco_completo = os.path.join(pasta_base, f"dendrograma_{nome_base}_cluster_de_numero_{k}.png")
    endereco_completo = endereco_completo.replace("__", "_")

    # Salvando a figura ajustada
    figure.savefig(endereco_completo, dpi=300, bbox_inches='tight')
    plt.close(figure)  # Fechando a figura especificamente

# print(gerar_grafico_dendrograma(endereco,
#                                 banco_de_dados,
#                                 distancias_otimas,
#                                 K,
#                                 populacao))

# REFERÊNCIA(S): ---

# [1] USER: TEW22.
# Hierarchical clustering - dendrograms using scipy adn scikit-learn in python.
# Available in: <https://www.youtube.com/watch?v=JcfIeaGzF8A>.
# YouTube.
# Accessed in: 18/04/2024 09:39.

# [2] USER: ARGUMENTED AI.
# Hierarchical clustering - fun and easy machine learning.
# Available in: <https://www.youtube.com/watch?v=EUQY3hL38cw>
# YouTube.
# Accessed in: 18/04/2024 09:39.
