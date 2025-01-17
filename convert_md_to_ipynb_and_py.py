# -*- coding: utf-8 -*-
import os
from nbconvert import MarkdownExporter, PythonExporter
import nbformat

def convert_md_to_ipynb(md_file):
    """
    Converte um arquivo Markdown (.md) para Jupyter Notebook (.ipynb).
    
    Args:
        md_file (str): Caminho para o arquivo Markdown.
    """
    # Lendo o conteúdo do arquivo .md
    with open(md_file, 'r', encoding='utf-8') as file:
        md_content = file.read()

    # Criando um notebook com o conteúdo do arquivo .md
    notebook = nbformat.v4.new_notebook()
    notebook.cells.append(nbformat.v4.new_markdown_cell(md_content))

    # Definindo o nome do arquivo de saída .ipynb
    ipynb_file = md_file.replace('.md', '.ipynb')

    # Escrevendo o notebook para um arquivo .ipynb
    with open(ipynb_file, 'w', encoding='utf-8') as file:
        nbformat.write(notebook, file)

    return ipynb_file

def convert_ipynb_to_py(ipynb_file):
    """
    Converte um arquivo Jupyter Notebook (.ipynb) para Python Script (.py).
    
    Args:
        ipynb_file (str): Caminho para o arquivo Jupyter Notebook.
    """
    # Lendo o notebook
    with open(ipynb_file, 'r', encoding='utf-8') as file:
        notebook = nbformat.read(file, as_version=4)

    # Criando um objeto PythonExporter
    python_exporter = PythonExporter()

    # Exportando o notebook para código Python
    python_code, _ = python_exporter.from_notebook_node(notebook)

    # Definindo o nome do arquivo de saída .py
    py_file = ipynb_file.replace('.ipynb', '.py')

    # Escrevendo o código Python no arquivo de saída
    with open(py_file, 'w', encoding='utf-8') as file:
        file.write(python_code)

    return py_file

# Definindo o nome do arquivo que deve ser excluído das subpastas
excluded_file = 'convert_md_to_ipynb.py'

# Obtendo o caminho absoluto da pasta raiz
root_path = os.path.abspath('.')

# Percorrendo todos os diretórios e subdiretórios a partir da pasta atual
for dirpath, dirnames, filenames in os.walk('.'):
    for filename in filenames:
        # Construindo o caminho completo do arquivo
        full_path = os.path.join(dirpath, filename)

        if filename.endswith('.md'):
            try:
                # Convertendo .md para .ipynb
                ipynb_file = convert_md_to_ipynb(full_path)

                # Convertendo .ipynb para .py
                py_file = convert_ipynb_to_py(ipynb_file)

                print(f'{full_path} foi convertido com sucesso para {ipynb_file} e {py_file}')

            except Exception as e:
                print(f'Erro ao processar {full_path}: {e}')

        # Verificando se o arquivo é o que deve ser excluído e se não está na pasta raiz
        elif filename == excluded_file and os.path.abspath(dirpath) != root_path:
            # Excluindo o arquivo
            os.remove(full_path)
            print(f'Arquivo excluído: {full_path}')

# %% [markdown]
# ## Referências
# 
# [1] OPENAI. ***Converter .md em .ipynb***
# Disponível em: <https://chatgpt.com/c/871d9945-f5cc-4dc6-a7bd-638186278592>.
# ChatGPT.
# Acessado em: 26/01/2024 11:35.
# 
