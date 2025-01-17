# %%
# -*- coding: utf-8 -*-


# %% [markdown]
# # Converter um arquivo do tipo Jupyter Notebook file (`.ipynb`) para Markdown (`.md`) e Python (`.py`)

# %% [markdown]
# ## Resumo
# 
# Este arquivo converte todos os arquivos com o nome `README.ipynb` para `.md` e `.py` a partir da pasta raiz e percorrendo as subpastas.
# 
# ## _Abstract_
# 
# _This file converts all files with the name `README.ipynb` to `.md` and `.py` starting from the root folder and traversing the subfolders._

# %% [markdown]
# # 1. Converter um arquivo do tipo Jupyter Notebook file (`.ipynb`) para Markdown (`.md`) e Python (`.py`)
# 
# Para executar o código fornecido em todos os arquivos `README.ipynb` na pasta raiz e subpastas, você precisará realizar executar o código abaixo. Uma abordagem eficaz é usar o módulo `os` do Python para percorrer todos os diretórios e subdiretórios, encontrando arquivos que correspondam ao nome `README.ipynb`. A seguir, apresento um exemplo de como você pode fazer isso:
# 
# Esse código utiliza `os.walk()` para percorrer todos os diretórios e subdiretórios da pasta atual (indicada por '.'). Ele verifica se algum dos arquivos nos diretórios é um `README.ipynb` e, em seguida, realiza o processo de conversão para Markdown, como especificado no seu código original. O caminho completo do arquivo é usado para garantir que o arquivo correto seja convertido, independente de onde ele esteja na estrutura de pastas.

# %%
# ! pip install nbconvert

# %%
import os
from nbconvert import MarkdownExporter, PythonExporter
import nbformat

# Definindo o nome do arquivo que deve ser excluído das subpastas
excluded_file = 'convert_ipynb_to_md.ipynb'

# Obtendo o caminho absoluto da pasta raiz
root_path = os.path.abspath('.')

# Percorrendo todos os diretórios e subdiretórios a partir da pasta atual
for dirpath, dirnames, filenames in os.walk('.'):
    for filename in filenames:
        # Construindo o caminho completo do arquivo
        full_path = os.path.join(dirpath, filename)

        if filename == 'README.ipynb':
            try:
                # Tentando ler o arquivo .ipynb para verificar se é um JSON válido
                with open(full_path, 'r') as file:
                    nbformat.read(file, as_version=4)

                # Criando um objeto MarkdownExporter
                markdown_exporter = MarkdownExporter()
                # Criando um objeto PythonExporter
                python_exporter = PythonExporter()

                # Exportando o arquivo .ipynb para código Markdown
                markdown_code, _ = markdown_exporter.from_filename(full_path)
                # Exportando o arquivo .ipynb para código Python
                python_code, _ = python_exporter.from_filename(full_path)

                # Definindo o nome do arquivo de saída .md
                markdown_output_filename = full_path.replace('.ipynb', '.md')
                # Definindo o nome do arquivo de saída .py
                python_output_filename = full_path.replace('.ipynb', '.py')

                # Escrevendo o código Markdown no arquivo de saída
                with open(markdown_output_filename, 'w') as file:
                    file.write(markdown_code)
                # Escrevendo o código Python no arquivo de saída
                with open(python_output_filename, 'w') as file:
                    file.write(python_code)

                print(f'{full_path} was successfully converted to {markdown_output_filename} and {python_output_filename}')

            except nbformat.reader.NotJSONError as e:
                print(f'Error processing {full_path}: File is not valid JSON - {e}')

        # Verificando se o arquivo é o que deve ser excluído e se não está na pasta raiz
        elif filename == excluded_file and os.path.abspath(dirpath) != root_path:
            # Excluindo o arquivo
            os.remove(full_path)
            print(f'Deleted file: {full_path}')


# %% [markdown]
# ## Referências
# 
# [1] OPENAI.
# ***Converter vários README.ipynb para .md e .py.***
# Disponível em: <https://chat.openai.com/c/50f64d4d-cfe7-40ac-a8aa-27ffa4eb5a5e>.
# ChatGPT.
# Acessado em: 26/01/2024 11:35.
