import os
import pandas as pd
import matplotlib.pyplot as plt
from data_loader import carregar_dados_csv  # Supondo que essa função já exista no seu código

# Caminho do arquivo CSV
caminho_arquivo_csv = r'C:\Users\fehao\Documents\hello-world\project_DataAnalyzer\arquivos\Pedidos-1.csv'

# Verificar se o arquivo existe antes de tentar carregá-lo
if not os.path.exists(caminho_arquivo_csv):
    print(f"Erro: O arquivo '{caminho_arquivo_csv}' não foi encontrado.")
else:
    try:
        # Carregar os dados
        dados = carregar_dados_csv(caminho_arquivo_csv)

        if dados is not None and not dados.empty:
            # Funções de análise e visualização
            def gerar_histograma(df, coluna):
                """
                Gera um histograma para uma coluna de um DataFrame com o contexto das vendas.

                Args:
                    df (pandas.DataFrame): DataFrame com os dados de vendas.
                    coluna (str): Nome da coluna para gerar o histograma.
                """
                plt.figure(figsize=(10, 6))
                plt.hist(df[coluna], bins=20, color='skyblue', edgecolor='black')
                plt.title(f'Distribuição das {coluna} Vendidas', fontsize=16)
                plt.xlabel(f'{coluna}', fontsize=14)
                plt.ylabel('Frequência', fontsize=14)
                plt.grid(True, linestyle='--', alpha=0.7)
                plt.show()

            def gerar_grafico_barras(df, coluna_categoria, coluna_valor):
                """
                Gera um gráfico de barras para o total de unidades vendidas por item ou vendedor.

                Args:
                    df (pandas.DataFrame): DataFrame com os dados de vendas.
                    coluna_categoria (str): Nome da coluna com as categorias.
                    coluna_valor (str): Nome da coluna com os valores.
                """
                df.groupby(coluna_categoria)[coluna_valor].sum().plot(kind='bar', color='lightcoral')
                plt.title(f'Total de {coluna_valor} por {coluna_categoria}', fontsize=16)
                plt.xlabel(coluna_categoria, fontsize=14)
                plt.ylabel(f'Total de {coluna_valor}', fontsize=14)
                plt.grid(True, linestyle='--', alpha=0.7)
                plt.show()

            # Exemplo de uso
            gerar_histograma(dados, 'Unidades')
            gerar_grafico_barras(dados, 'Item', 'Unidades')
        else:
            print("Erro: O arquivo CSV está vazio ou não foi carregado corretamente.")
    except Exception as e:
        print(f"Ocorreu um erro ao processar os dados: {e}")
