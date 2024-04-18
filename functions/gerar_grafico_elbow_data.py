import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

def gerar_grafico_elbow_data(endereco,
                             num_de_k_inicial,
                             k_large,
                             WSs_total_otimo,
                             num_max_I):
    """
    Gera e salva o gráfico Elbow com base nos dados fornecidos.
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
        valor = txt if np.isscalar(txt) else txt.item()
        subcharts.annotate(f'{valor:.2f}', (x[i], valor), size=10)

    # Configuração dos limites, labels e título
    subcharts.set_xlim([0, k_large + 1])
    subcharts.set_xlabel("$ k $")
    subcharts.set_ylabel("$ WS_{Total} $ Normalizado")
    subcharts.set_title(r"Elbow Data Chart")
    subcharts.xaxis.set_major_locator(MaxNLocator(integer=True))

    plt.tight_layout()

    # Encontrar o caminho para a pasta 'outputs' dentro de 'k_means'
    caminho_base = os.path.dirname(endereco)  # Assume que 'endereco' aponta para dentro de 'k_means'
    pasta_outputs = os.path.join(caminho_base, 'outputs')

    # Processamento do nome base
    nome_base = os.path.splitext(os.path.basename(endereco))[0].replace("__", "_") + \
        "_de_" + str(num_de_k_inicial) + "_ate_" + str(k_large) + "_clusters_com_" + str(num_max_I) + "_iteracoes"
    nome_base_parts = nome_base.split('_')

    # Remover a última parte se for numérica
    if nome_base_parts[-1].isdigit():
        nome_base = '_'.join(nome_base_parts[:-1])

    # Criação do diretório de saída se não existir
    pasta_base = os.path.join(pasta_outputs, nome_base)
    pasta_base = pasta_base.replace("__", "_")
    if not os.path.exists(pasta_base):
        os.makedirs(pasta_base)

    # Caminho completo do arquivo de saída
    endereco_completo = os.path.join(pasta_base, f"elbow_data_chart_{nome_base}_cluster_de_numero_{k_large}.png")
    endereco_completo = endereco_completo.replace("__", "_")

    # Salvando a figura ajustada
    figure.savefig(endereco_completo, dpi=300, bbox_inches='tight')
    plt.close(figure)

# A função pode ser chamada da seguinte forma:
# gerar_grafico_elbow_data(endereco, num_de_k_inicial, k_large, WSs_total_otimo_lista, num_max_I)
