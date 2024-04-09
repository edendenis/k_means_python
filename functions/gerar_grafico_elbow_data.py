import numpy as np
import matplotlib.pyplot as plt
import pickle as pkl
from matplotlib.ticker import MaxNLocator

# Ler os objetos:
# with open("objetos.pkl", "rb") as f:
#     endereco, \
#     num_de_k_inicial, \
#     k_large, \
#     WSs_total_otimo_lista, \
#     banco_de_dados, \
#     distancias_otimas, \
#     populacao,\
#     ks_min_otimos = pkl.load(f)

import numpy as np
import os
import pickle as pkl

from matplotlib.ticker import MaxNLocator
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

import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib.ticker import MaxNLocator

def gerar_grafico_elbow_data(endereco,
                             num_de_k_inicial,
                             k_large,
                             WSs_total_otimo,
                             num_max_I):
    """
    Gera e salva o gráfico Elbow com base nos dados fornecidos.

    :param endereco: Endereço do banco de dados. str.
    :param num_de_k_inicial: Número inicial de clusters. int.
    :param k_large: Número total de clusters. int.
    :param WSs_total_otimo: Lista com a soma total de quadrados dentro dos clusters. list.
    :param k_large: Número total de cluster. int. 
    :param num_max_I: Número máximo de iterações. int.
 
    :return: Gráfico do Elbow Data. object.
    """

    plt.close('all')

    # Normalizar os dados
    WSs_total_otimo_normalizado = WSs_total_otimo / np.max(WSs_total_otimo)

    # Gerar o gráfico Elbow
    x = np.arange(num_de_k_inicial, k_large + 1, 1)
    [figure, subcharts] = plt.subplots(figsize=(24, 11))

    # Plotar os dados
    subcharts.plot(x, WSs_total_otimo_normalizado, color="b", marker="o", linestyle="-")

    # Anotações em cada ponto do gráfico
    for i, txt in enumerate(WSs_total_otimo_normalizado):
        # Converter cada elemento para escalar se for um array numpy de um elemento
        valor = txt if np.isscalar(txt) else txt.item()
        subcharts.annotate(f'{valor:.2f}', (x[i], valor), size=10)

    # Configuração dos limites, labels e título
    subcharts.set_xlim([0, k_large + 1])
    subcharts.set_xlabel("$ k $")
    subcharts.set_ylabel("$ WS_{Total} $ Normalizado")
    subcharts.set_title(r"Elbow Data Chart")

    # Configurar a localização dos marcadores no eixo x para serem números inteiros
    subcharts.xaxis.set_major_locator(MaxNLocator(integer=True))

    # Ajuste automático do layout
    plt.tight_layout()

    # Processamento do nome base para remoção de segmentos numéricos no final
    nome_base = os.path.splitext(os.path.basename(endereco))[0].replace("__", "_") + \
        "_de_" + str(num_de_k_inicial) + "_ate_" + str(k_large) + "_clusters_com_" + str(num_max_I) + "_iteracoes"
    nome_base_parts = nome_base.split('_')

    # Remover a última parte se for numérica
    if nome_base_parts[-1].isdigit():
        nome_base = '_'.join(nome_base_parts[:-1])

    # Criação do diretório de saída se não existir
    pasta_base = os.path.join('outputs', nome_base)
    if not os.path.exists(pasta_base):
        os.makedirs(pasta_base)

    # Caminho completo do arquivo de saída
    endereco_completo = \
        os.path.join(pasta_base, f"elbow_data_chart_{nome_base}_cluster_de_numero_{k_large}.png")
    
    # Salvando a figura ajustada
    figure.savefig(endereco_completo, dpi=300, bbox_inches='tight')
    plt.close(figure)  # Fechando a figura especificamente

# A função pode ser chamada da seguinte forma:
# gerar_grafico_elbow_data(endereco, num_de_k_inicial, k_large, WSs_total_otimo_lista)
