<!-- LOGOTIPO DO PROJETO -->
<div style="display: flex; justify-content: center;">
   <a href="https://github.com/othneildrew/Best-README-Template">
     <img src="figures/logotipo_edf_vetorizado_fundo_roxo_e_nome.png" alt="Logo" width="80" height="80">
   </a>
</div>

<h3 align="center">EDF k-means Python</h3>

<div style="display: flex; justify-content: center;">
  <a href="https://zenodo.org/doi/10.5281/zenodo.10668919">
    <img src="https://zenodo.org/badge/758237447.svg" alt="DOI">
  </a>
</div>

<p align="center">
 A aplicação de computação para o algoritmo k-means é uma técnica de agrupamento não supervisionado que organiza os dados em agrupamentos com base na similaridade. Ele atribui iterativamente pontos de dados aos centróides e recalcula os centróides com base na média dos pontos atribuídos até que a variação entre pontos e centróides seja minimizada.
 <br />
 <a href="https://github.com/edendenis/k_means_python"><strong>Explore os documentos »</strong></a>
 <br />
 <br />
 <a href="https://github.com/edendenis/k_means_python">Ver demonstração</a>
 ·
 <a href="https://github.com/edendenis/k_means_python">Relatar bug</a>
 ·
 <a href="https://github.com/edendenis/k_means_python">Solicitar recurso</a>
</p>


## Resumo

A aplicação de computação para o algoritmo k-means é uma técnica de agrupamento não supervisionado que organiza os dados em agrupamentos com base na similaridade. Ele atribui iterativamente pontos de dados aos centróides e recalcula os centróides com base na média dos pontos atribuídos até que a variação entre pontos e centróides seja minimizada.

## _Abstract_

_The computing application for the k-means algorithm is an unsupervised clustering technique that organizes data into groupings based on similarity. It iteratively assigns data points to centroids and recalculates the centroids based on the average of the assigned points until the variation between points and centroids is minimized._

### Construído com

Esta seção deve listar todas as principais estruturas/bibliotecas usadas para inicializar seu projeto. Deixe quaisquer complementos/plugins para a seção de agradecimentos. Aqui estão alguns exemplos.

* [![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
* [![Anaconda](https://img.shields.io/badge/Anaconda-44A833?style=flat-square&logo=anaconda&logoColor=white)](https://www.anaconda.com/)

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

<!-- COMEÇANDO -->
### Começando

Este é um exemplo de como você pode dar instruções sobre como configurar seu projeto localmente.
Para obter uma cópia local instalada e funcionando, siga estas etapas simples de exemplo.

### Pré-requisitos

Este é um exemplo de como listar os itens necessários para usar o software e como instalá-los.
* Python 3.8
* Anaconda 24.1.0
* Git
* IDE para executar o arquivo `.ipynb` (PyCharm, Spyder, VS Code etc.)

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>


## Guia de instalação

### Instalar o Git

Verifique se você tem o Git instalado no seu computador. Se não tiver, você pode baixá-lo e instalá-lo a partir do site oficial do Git: https://git-scm.com/downloads

Abra o Git Bash. Você pode fazer isso clicando com o botão direito do mouse em qualquer diretório e selecionando a opção "Git Bash Here" no menu de contexto.

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

## Guia de instalação

### Instalar o Git

Verifique se você tem o Git instalado no seu computador. Se não tiver, você pode baixá-lo e instalá-lo a partir do site oficial do Git: https://git-scm.com/downloads

Abra o Git Bash. Você pode fazer isso clicando com o botão direito do mouse em qualquer diretório e selecionando a opção "Git Bash Here" no menu de contexto.

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

#### `Windows` [2]

Para gerar uma chave SSH no Windows para uso no GitLab, você pode seguir as etapas abaixo:

1. Verifique se você tem o Git instalado no seu computador. Se não tiver, você pode baixá-lo e instalá-lo a partir do site oficial do Git: https://git-scm.com/downloads

2. Abra o Git Bash. Você pode fazer isso clicando com o botão direito do mouse em qualquer diretório e selecionando a opção "Git Bash Here" no menu de contexto.

3. No Git Bash, digite o seguinte comando para gerar uma nova chave SSH `ssh-keygen -t rsa -C "seu_email@exemplo.com"` (`@gitlab.com`)

Certifique-se de substituir `seu_email@exemplo.com` pelo seu endereço de e-mail associado à sua conta do GitLab. Você pode deixar a senha em branco pressionando Enter duas vezes.

4. Será solicitado que você forneça um local para salvar a chave. Você pode simplesmente pressionar Enter para aceitar o local padrão (geralmente `C:\Usuários\SeuNome.ssh\id_rsa`).

5. O comando irá gerar a chave SSH pública e privada. Por padrão, a chave pública será salva como `id_rsa.pub`.

6. Agora, você precisa adicionar a chave SSH pública à sua conta do GitLab. Abra o GitLab no seu navegador e faça login na sua conta.

7. No canto superior direito da página, clique na sua foto de perfil e vá para `Settings` (Configurações) no menu suspenso.

8. No menu lateral esquerdo, clique em `SSH Keys` (Chaves SSH).

9. No campo 'Key', abra o arquivo `id_rsa.pub` (ou qualquer nome que você tenha dado à sua chave pública) que você gerou anteriormente. Copie todo o conteúdo do arquivo e cole no campo "Key" no GitLab.

10. Dê um nome para a chave, por exemplo, `Meu Computador` e clique em `Add Key` (Adicionar chave).

Agora você gerou e adicionou com sucesso uma chave SSH para uso no GitLab. Você poderá usar essa chave para autenticar suas operações do GitLab usando o Git no Windows.

Depois de copiar a chave pública, você poderá fazer login no servidor remoto sem precisar digitar a senha toda vez, desde que a chave privada esteja presente no sistema local e a frase secreta (se fornecida) esteja correta.

Lembre-se de proteger sua chave privada e evitar compartilhá-la com outras pessoas. É recomendável usar autenticação por chave SSH em vez de senhas, pois oferece uma camada adicional de segurança.

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

### Atualizar pacotes `pip` e `setuptools` [3]

É recomendado que sejam atualizado os pacotes, como segue:

1. **Verificar a versão do `pip`:** Verifique se você está usando uma versão atualizada do `pip`. Execute o seguinte comando para atualizá-lo, caso necessário: `pip install --upgrade pip`

2. **Verificar a versão do `setuptools`:** Verifique se você possui a versão mais recente do pacote `setuptools` instalada. Execute o seguinte comando para atualizá-lo, se necessário:`pip install --upgrade setuptools`

3. **Verificar a versão do `wheel`:** O erro menciona que a opção `bdist_wheel` é inválida. Isso pode acontecer se o pacote `wheel` estiver desatualizado. Execute o seguinte comando para atualizar o pacote `wheel` com o comando: `pip install --upgrade wheel`

4. É recomendado reiniciar o Sistema Operacional (SO).

### Clonar o repositório do Git e instalar o pacote `proplib`

#### `Linux`

1. **Clone o repositório:**

  - **Pelo terminal:** `git clone git@github.com:edendenis/k_means_python.git`

  - **(Ou)** Fazer o _download_ do repositório `.zip` pela página web do GitHub, botão ao lado do botão azul `clone` à direita

  <p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

#### `Windows`

1. **Clone o repositório:**

  - **Pelo terminal:** `git clone git@github.com:edendenis/rbf_python.git`

  - **(Ou) Fazer o _download_ do repositório `.zip` pela página web do GitHub, botão ao lado do botão azul `clone` à direita

  <p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

## Como executar a aplicação

1. Abrir o arquivo `main_k_means.ipynb` o qual está com comentários;

2.Dentro do arquivo `main_k_means.py`, na Seção `Carregamento, armazenamento e manipulação de dados`, alterar o caminho para o banco de dados que deverá ser utilizado para a execução, por exemplo:

    ```
    # CARREGAMENTO, ARMAZENAMENTO E MANIPULAÇÃO DO DADOS: ---
    endereco = "databases/aeronaves_militares_arbitrado_sem_data_de_entrada_de_operacao.xlsx"
    ```

3. A partir daqui, você pode optar por executar o código pelo `Terminal Emulator` ou através de um editor como o `PyCharm`, `Spyder` e/ou `VS Code`, como segue.

### Executar a partir do `Terminal Emulator`

1. **Digitar o 'Número do k inicial'**: Como por exemplo: `Digitar o 'Número do k inicial' = 2`
    
    - Trata-se de um número inteiro **NÃO** negativo;

    - É recomendado o mínimo de `2` ou;

    - Caso queira executar a aplicação para um único k-_cluster_, o número dk `k inicial` será igual o `Número total de k-_clusteres` que será solicitado no Item a seguir.

2 **Digitar o 'Número total de k-clusters'**: Como por exemplo: `Digitar o 'Número de total de k-clusters' = 20`
    
    - Trata-se de um número inteiro **NÃO** negativo;
    
    - É recomendado um número mínimo, por exemplo, `10`, `15` ou `20` para que `Elbow Data Chart` (Gráfico de Dados de Cotovelo) indique o número de k-_clusteres_ idela que os dados devem ser agrupados. Tudo isso será indicado pela "quina" gerada pelo gráfico, por exemplo.

3 **Digitar o 'Número total de iterações'**: Como por exemplo: `Digitar o 'Número total de iterações' = 1000`
    
    - Trata-se de um número inteiro **NÃO** negativo;
    
    - É recomendado um número mínimo de, pelo menos, `1000` iterações, e qual pode e deve ser alterada para valores maiores (`2000`, `4000`, `8000` etc.) em execuções posteriores, para validar se os resultados convergem.
    
    - Em geral, a aplicação é executada em minutos para a maior parte dos problemas, mas cade ao usuário, ajustar à sua necessidade, mesmo que "perca" na precisão da solução, mas ganhe no custo computacional (tempo).

4 **Digitar o 'Título do Eixo x do Dendrograma'**: Como por exemplo: `Digitar o 'Título do Eixo x do Dendrograma': Aeronaves militares`

    - Trata-se de um texto;

5. Os resultados, ou seja, dados de saída (_outputs_), serão salvos na subpasta `outputs/` que está dentro do projeto.

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>


<!-- LICENÇA -->
## Licença

Distribuído sob a licença MIT. Consulte `LICENSE.txt` para obter mais informações.

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

<!-- ROTEIRO -->
## Roteiro

- [x] Adicionar registro de alterações
- [x] Adicionar links de volta ao topo
- [x] Adicionar modelos adicionais com exemplos
- [x] Suporte multilíngue
     - [x] Espanhol
     - [x] Inglês
     - [x] Português
     - [x] Português brasileiro 

Consulte os [problemas abertos](https://github.com/edendenis/k_means_python/issues) para obter uma lista completa dos recursos propostos (e problemas conhecidos).

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>


<!-- CONTRIBUIÇÔES -->
## Contribuições

As contribuições são o que tornam a comunidade de código aberto um lugar incrível para aprender, inspirar e criar. Qualquer contribuição que você fizer será **muito apreciada**.

Se você tiver uma sugestão que possa melhorar isso, bifurque o repositório e crie uma solicitação `pull`. Você também pode simplesmente abrir um problema com a tag “aprimoramento”.
Não se esqueça de dar uma estrela ao projeto! Obrigado novamente!

1. Bifurque o projeto
2. Crie sua ramificação de recursos (`git checkout -b feature/AmazingFeature`)
3. Confirme suas alterações (`git commit -m 'Add some AmazingFeature'`)
4. Envie para a filial (`git push origin feature/AmazingFeature`)
5. Abra uma solicitação pull

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Agradecimentos

* [Best README Template](https://github.com/othneildrew/Best-README-Template?tab=readme-ov-file)
* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>


## Referências

[1] RICIERI, A. P. ***Curso de big data de lousa***. Prandiano - Museu da Matemática, São Paulo, 2018.

[2] LINNAEUS, C. v. ***Systema naturae per regna tria naturae***. secundum classes, ordines, genera, species, cum characteribus, differentiis, synonymis, locis, 1758.

[3] BAUMAN, Z. ***Liquid modernity***. Polity Press, 2000. ISBN 0745624103.

[4] MACQUEEN, J. ***Methods for classification and analysis of multivariate observations***. volume 28: (1967), páginas 250–274. ISSN 0883-7252. doi:10.1002/jae.1272.

[5] RUSSELL, S.; NORVIG, P. ***Artificial intelligence: a modern approach***. Prentice Hall, 2 edição, 2002. ISBN 978-0137903955.

[6] BERK, K. N.; KHATTREE, R.; NAIK, D. ***Applied multivariate statistics with sas software***. volume 54, 2000. doi:10.2307/2686040.

[7] ANDERBERG, M. R.. ***Cluster analysis for applications***. 1973.

[8] MANKTELOW, M.. ***History of taxonomy***. Uppsala University, 2010.

[9] ***An update of the angiosperm phylogeny group classification for the orders and families of the flowering plants***. Botanical Journal of The Linnean Society, volume 161: (2009), página 105. ISSN 0024-4074. doi:10.1111/j.1095-8339.2009.00996.x.

[10] SILVA, B. M.; FREGNANI, J. A. T. G.; MAGALHÃES, P. E. C. S. ***Frontiers in aerospace science: conceptual design of green transport airplanes***. Bentham Book, 2018.

[11] USUÁRIO:REI-ARTHUR. ***Airbus a380***. Disponível em: <https://pt.wikipedia.org/wiki/Airbus_A380>. Acessado em: 26/10/2018 09:55.

[12] ***Os aviões com maior número de vítimas***. Disponível em: <https://www.terra.com.br/noticias/infograficos/ranking-desastres-aereos/05.htm>. Acessado em: 26/10/2018 13:04.

[13] USUÁRIO:REI-ARTHUR. ***Embraer e-jets e2***. Disponível em: <https://pt.wikipedia.org/wiki/Embraer_E-Jets_E2>. Acessado em: 30/10/2018 09:56.

[14] USUÁRIO:REI-ARTHUR. ***Lockheed martin f-22***. Disponível em: <https://pt.wikipedia.org/wiki/Lockheed_Martin_F-22>. Acessado em: 26/10/2018 16:37.

[15] USUÁRIO:REI-ARTHUR. ***Embraer emb-314***. Disponível em: <https://pt.wikipedia.org/wiki/Embraer_EMB-314>. Acessado em: 30/10/2018 07:09.

[16] USUÁRIO:REI-ARTHUR. ***North american p-51 mustang***. Disponível em: <https://pt.wikipedia.org/wiki/North_American_P-51_Mustang>. Acessado em: 30/10/2018 05:03.

[17] KIUSALAAS, J.. ***Numerical methods in engineering with python***. 2nd ed. edição, 2010.

[18] LANGTANGEN, H. P.. ***Python scripting for computational science***. Berlin Heidelberg, 3th ed. edição, 2009.

[19] MCKINNEY, W.. ***Python para análise de dados: tratamento de dados com pandas, numpy e ipython***. São Paulo, 1a ed. edição, 2018.

[20] TEAM, W. M. P. D.. ***Pandas: powerful python data analysis toolkit***. 2018.

[21] RAMALHO, L.. ***Python fluente***. São Paulo, 1a ed. edição, 2018.

[22] GRUS, J.. ***Data science do zero***. Rio de Janeiro, 1a ed. edição, 2009.

[23] COMMUNITY. ***Scipy.cluster.hierarchy.dendrogram***. Disponível em: <https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.dendrogram.html>. Acessado em: 2018-

