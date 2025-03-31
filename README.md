# Project_DataAnalyze
Este projeto tem como objetivo realizar análise de dados de vendas. A partir de um arquivo CSV contendo informações sobre as vendas de produtos, o sistema processa e gera relatórios detalhados, além de apresentar visualizações gráficas para ajudar a entender os padrões e tendências.

# DataAnalyzer - Projeto de Análise de Dados em Python

Este projeto foi desenvolvido como um exercício prático para aplicar e aprimorar minhas habilidades em análise de dados com Python. O projeto lê dados de um arquivo CSV, realiza análises estatísticas básicas, gera visualizações e cria relatórios em formato de texto.

## Funcionalidades

* **Leitura de dados:** Carrega dados de arquivos CSV usando a biblioteca pandas.
* **Análise de dados:** Calcula estatísticas descritivas (média, mediana, desvio padrão, etc.) e realiza análises específicas (total de vendas por item).
* **Visualização de dados:** Gera histogramas e gráficos de barras usando a biblioteca matplotlib.
* **Geração de relatórios:** Cria relatórios em formato de texto com os resultados da análise.

## Estrutura do Projeto

* `arquivos/`: Pasta contendo o arquivo CSV de dados (`Pedidos-1.csv`).
* `venv/`: Ambiente virtual Python com as bibliotecas necessárias.
* `data_analyzer.py`: Funções para análise de dados.
* `data_loader.py`: Funções para carregar dados de arquivos CSV.
* `data_visualizer.py`: Funções para gerar visualizações.
* `report_generator.py`: Funções para gerar relatórios.
* `requirements.txt`: Lista de bibliotecas Python necessárias.
* `utils.py`: Funções utilitárias.
* `main.py`: Script principal que orquestra a execução do programa.

## Como Executar

1.  Clone o repositório.
2.  Crie e ative um ambiente virtual: `python -m venv venv` e `source venv/bin/activate` (Linux/macOS) ou `venv\Scripts\activate` (Windows).
3.  Instale as dependências: `pip install -r requirements.txt`.
4.  Execute o script principal: `python main.py`.

## Observações

* Este projeto foi desenvolvido como um exercício de aprendizado e pode ser expandido e adaptado para analisar diferentes tipos de dados e realizar análises mais complexas.
* Contribuições e sugestões são bem-vindas!

## Licença

Este projeto está sob a licença [MIT](LICENSE) - veja o arquivo [LICENSE.md](LICENSE.md) para detalhes.
