import numpy as np
import pandas as pd
import pickle as pkl
import os as os

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

def gerar_relatorio_em_planilha(endereco, banco_de_dados, distancias_otimas, ks_min_otimos, k):
    """
    :param endereco: Endereço do arquivo de entrada, incluindo o caminho completo e a extensão.
    :param banco_de_dados: Banco de dados em forma de DataFrame ou estrutura compatível.
    :param distancias_otimas: Array de distâncias ótimas para serem normalizadas.
    :param ks_min_otimos: Arranjo contendo os k-clusters mínimos ótimos.
    :param k: Número de k-clusters.
    :return: None. Gera um arquivo Excel com os resultados.
    """

    # Normalizar os dados
    distancias_otimas = distancias_otimas / np.max(distancias_otimas)

    # Criar DataFrame dos elementos associados
    elementos_associados = np.concatenate((np.round(distancias_otimas, 3), ks_min_otimos), axis=1)
    elementos_associados = pd.DataFrame(elementos_associados)

    # Criar DataFrame do banco de dados
    banco_de_dados = pd.DataFrame(banco_de_dados)
    dados_a_serem_analisados = banco_de_dados.iloc[:, 0]

    # Atualizar DataFrame dos elementos associados
    elementos_associados = pd.DataFrame(np.array(elementos_associados),
                                        index=dados_a_serem_analisados,
                                        columns=["Distâncias ótimas normalizadas", "Próximo de"])
    elementos_associados = elementos_associados.sort_values(by=["Próximo de"], ascending=True)

    # Exibir o DataFrame resultante
    print(elementos_associados)

    # Extrair o nome base do arquivo de entrada do endereco
    nome_base = os.path.splitext(os.path.basename(endereco))[0]

    # Se o nome_base terminar com um sublinhado, removemos ele
    if nome_base.endswith('_'):
        nome_base = nome_base[:-1]

    # A pasta base será 'outputs' combinada com o nome base do arquivo
    pasta_base = os.path.join('outputs', nome_base)
    if not os.path.exists(pasta_base):
        os.makedirs(pasta_base)

    # O arquivo será salvo dentro da pasta correspondente ao nome do arquivo de entrada
    nome_arquivo = f"{nome_base}_{k}.xlsx"
    endereco_completo_arquivo = os.path.join(pasta_base, nome_arquivo)

    # Criação do ExcelWriter e salvamento do arquivo
    pasta_de_trabalho = pd.ExcelWriter(endereco_completo_arquivo, engine='xlsxwriter')
    elementos_associados.to_excel(pasta_de_trabalho, sheet_name='elementos_associados')

    # Fechar o exportador Pandas Excel e salvar o arquivo Excel
    pasta_de_trabalho.close()

# print(gerar_relatorio_em_planilha(endereco,
#                                 banco_de_dados,
#                                 distancias_otimas,
#                                 ks_min_otimos,
#                                 K))
