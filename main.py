import os
from data_loader import carregar_dados_csv
from data_analyzer import calcular_estatisticas_descritivas, calcular_total_vendas_por_item
from data_visualizer import gerar_histograma, gerar_grafico_barras
from report_generator import gerar_relatorio_texto

# Caminho do arquivo CSV
caminho_arquivo_csv = r'C:\Users\fehao\Documents\hello-world\project_DataAnalyzer\arquivos.csv\Pedidos-1.csv'

# Verificar se o arquivo existe antes de tentar carregá-lo
if not os.path.exists(caminho_arquivo_csv):
    print(f"Erro: O arquivo '{caminho_arquivo_csv}' não foi encontrado.")
else:
    try:
        # Carregar os dados
        dados = carregar_dados_csv(caminho_arquivo_csv)

        if dados is not None and not dados.empty:
            # Verificar se as colunas esperadas estão presentes
            colunas_necessarias = {'Unidades', 'Item'}
            if not colunas_necessarias.issubset(dados.columns):
                print("Erro: O arquivo CSV não contém as colunas esperadas:", colunas_necessarias)
            else:
                # Analisar os dados
                estatisticas = calcular_estatisticas_descritivas(dados)
                total_vendas_item = calcular_total_vendas_por_item(dados)

                # Exibir os resultados no console
                print("Estatísticas Descritivas:")
                print(estatisticas)

                print("\nTotal de Vendas por Item:")
                print(total_vendas_item)

                # Gerar visualizações
                gerar_histograma(dados, 'Unidades')
                gerar_grafico_barras(dados, 'Item', 'Unidades')

                # Gerar relatório
                gerar_relatorio_texto(estatisticas, total_vendas_item)
        else:
            print("Erro: O arquivo CSV está vazio ou não foi carregado corretamente.")
    except Exception as e:
        print(f"Ocorreu um erro ao processar os dados: {e}")
