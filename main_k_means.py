# coding: utf-8
"""
Fundação Universidade Federal do ABC

Trabalho de Graduação em Engenharia III

Data de Criação: 06/03/2018
Data da última modificação: 28/09/2018
"""
# REVISÃO(ÕES): ---

# FUNÇÃO DO APLICATIVO: ---

# Função: classificar.

# PACOTE(S): ---

import time as time
import numpy as np
import pandas as pd
import os as os
import pickle as pkl
import functions.validacoes_das_variaveis as vv
import functions.k_means as km
import functions.gerar_grafico_elbow_data as ed
import functions.gerar_relatorio_dos_clusteres as re
import functions.gerar_grafico_dendrograma as de
# Comentei para poder ser executado também em Sistemas Operacionais Linux:
# import winsound as winsound

# CARREGAMENTO, ARMAZENAMENTO E MANIPULAÇÃO DO DADOS: ---

# Caminho para o diretório onde o script está localizado
script_dir = os.path.dirname(__file__)

endereco = "databases/injetores_l25.xlsx"

# Definindo o caminho completo para salvar o arquivo
endereco = os.path.join(script_dir, endereco)

banco_de_dados = pd.read_excel(endereco,
                               sheet_name=0)

bd_auxiliar = banco_de_dados

bd_auxiliar.columns = \
    bd_auxiliar.columns.str.replace(" ", "_")
bd_auxiliar.columns = \
    bd_auxiliar.columns.str.replace("-", "_")
bd_auxiliar.columns = \
    bd_auxiliar.columns.str.replace("__", "_")
# print(bd_auxiliar.head())

# A primeira coluna é removida, pois trata-se do "Nome da Aeronave"
bd_auxiliar = \
    bd_auxiliar.drop(bd_auxiliar.columns[0], axis = 1)
# A primeira coluna é removida, pois trata-se da
# "Data de Entrada de Operação"
# bd_auxiliar = \
#     bd_auxiliar.drop(bd_auxiliar.columns[0], axis = 1)

print("---")
print("DADO(S):")
print("")
print(bd_auxiliar.head())

print("")
print(bd_auxiliar.shape)

# VARIÁVEL(IS): ---

print("---")
print("\nVARIÁVEL(IS):")
# print("")

# sementes = Sementes do BIG Data
sementes = bd_auxiliar.values

# n = Número total de elementos
n = sementes.shape[0]

# num_de_variaveis = Número de variáveis
num_de_variaveis = sementes.shape[1]

# print(sementes)
# print(sementes.shape)

# digitar k-clusters;
num_de_k_inicial = input("\nDigitar o 'Número do k inicial' = ")
descricao = "Número do k inicial"
num_de_k_inicial = \
    vv.validar_variavel_inteira_nao_negativa(num_de_k_inicial, descricao)
# print("Número do k Inicial =", num_de_k_inicial)

# K = Número total de clusters
K = input("\nDigitar o 'Número total de k-clusters' = ")
descricao = "Número total k-clusters"
K = vv.validar_variavel_inteira_nao_negativa(K, descricao)
# Condição para não gerar mais grupos do que elementos
porcentagem = 0.80
if K >= porcentagem * n:
    print("Espeficique um valor de "
          "'Número Total K de k-clusters' menor que",
          int(porcentagem * n))
    quit()
# print("Número total K de k-clusters =", K)

# num_max_I = Número máximo de iterações
num_max_I = input("\nDigitar o 'Número total de iterações' = ")
descricao = "Número total de iterações"
num_max_I = \
    vv.validar_variavel_inteira_nao_negativa(num_max_I, descricao)
# print("Número máximo de iterações =", num_max_I)

# Validação do número inicial de k-clusteres:
if num_de_k_inicial <= 1 or num_de_k_inicial > K:
    print("Espeficique um valor de "
          "'Número do k inicial' maior que 1 (um)"
          "e menor que o 'Número Total K de k-clusters'.")
    quit()

titulo_do_eixo_x_do_dendrograma = input("\nDigitar o "
                                        "'Título do Eixo x do Dendrograma': ")

# populacao = População máxima a ser exibida no gráfico Dendrograma
populacao = input("\nDigitar o 'Número máximo da população a ser exibida no gráfico Dendrograma' = ")
descricao = "Número máximo da população a ser exibida no gráfico Dendrograma"
populacao = \
    vv.validar_variavel_inteira_nao_negativa(populacao, descricao)
# print("Número máximo da população a ser exibida no gráfico Dendrograma =", populacao)

# CÁLCULO(S): ---

tempo_inicio = time.time()
tempo_inicio_CPU = time.perf_counter()

# os medioides_otimos devem ser um arranjo
medioides_otimos_lista = []
ks_min_otimos_lista = []
WSs_total_otimo_lista = []

for k in range(num_de_k_inicial, K + 1, 1):
    [distancias_otimas, medioides_otimos, \
    ks_min_otimos, WS_total_otimo] = \
        km.k_means(num_de_k_inicial, k, sementes, num_max_I)
    medioides_otimos_lista.append(medioides_otimos)
    ks_min_otimos_lista.append(ks_min_otimos)
    WSs_total_otimo_lista.append(WS_total_otimo)

    # RESULTADO(S): ---
    print("\n---")
    print("RESULTADO(S) PARA k = " + str(k) + ":")
    print("")

    # print("Medioides ótimos:\n")
    # print(medioides_otimos)
    # print(medioides_otimos_lista)
    # print("")

    # Gerar relatório dos clusteres em planilha:
    endereco = endereco.replace("databases/", "")
    endereco = endereco.replace(".xlsx", "_")
    re.gerar_relatorio_dos_clusteres(endereco,
                                    banco_de_dados,
                                    distancias_otimas,
                                    ks_min_otimos,
                                    num_de_k_inicial,
                                    k,
                                    K,
                                    num_max_I)

    # print("")
    # print("WS total ótimo:")
    # print(WSs_total_otimo_lista)
    # print("")

    # Gráfico(s):

    # Plotar Dendrograma:
    if n <= populacao:
        populacao = n

    # for populacao in range(2, n + 1, 1): Caso se queira executar
    # o programa para gerar is elbow data charts para cada valor
    # de população

    if endereco.endswith("_") == True:
        endereco = endereco[:-1]
    endereco_antigo = endereco
    de.gerar_grafico_dendrograma(endereco,
                                 banco_de_dados,
                                 distancias_otimas,
                                 num_de_k_inicial,
                                 k,
                                 populacao,
                                 titulo_do_eixo_x_do_dendrograma,
                                 K,
                                 num_max_I)
    endereco = endereco_antigo

# Plotar o Elbow Data Chart:
ed.gerar_grafico_elbow_data(endereco,
                            num_de_k_inicial,
                            K,
                            WSs_total_otimo_lista,
                            num_max_I)

# Comentei para poder ser executado também em Sistemas Operacionais Linux:
# frequencia = 2500 # (Hertz)
# duracao = 1000 # (ms)
# winsound.Beep(frequencia, duracao)

print("\n---")
tempo_fim = time.time() - tempo_inicio
tempo_final_CPU = time.perf_counter()
print(f"Tempo de execução: {tempo_fim:.4f} [s]")
print(f"Tempo de execução (CPU): {tempo_final_CPU - tempo_inicio_CPU:.4f} [s]")

# Os objetos estão sendo salvos para NÃO ter que executar
# todo o código novamente, simplemente para executar
# a function abaixo
# Salvar os objetos:
# with open("objetos.pkl", "wb") as f:
#     pkl.dump([endereco,
#               num_de_k_inicial,
#               K,
#               WSs_total_otimo_lista,
#               banco_de_dados,
#               distancias_otimas,
#               populacao,
#               ks_min_otimos],
#              f)

# REFERÊNCIA(S): ---

# [1] MacQueen.
# [2] Ricieri
# [3] Livros de Python
