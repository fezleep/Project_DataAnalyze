def gerar_relatorio_texto(estatisticas, total_vendas_item, caminho_arquivo='relatorio.txt'):
    """
    Gera um relatório em formato de texto contendo estatísticas descritivas e total de vendas por item.

    Args:
        estatisticas (pandas.DataFrame or None): DataFrame com as estatísticas descritivas.
        total_vendas_item (pandas.Series or None): Series com o total de vendas por item.
        caminho_arquivo (str, opcional): Caminho para salvar o relatório. Padrão é 'relatorio.txt'.

    Returns:
        None
    """
    try:
        with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
            arquivo.write("===== Relatório de Análise de Dados =====\n\n")

            if estatisticas is not None:
                arquivo.write("### Estatísticas Descritivas ###\n")
                arquivo.write(estatisticas.to_string())  # Melhor formatação para DataFrame
                arquivo.write("\n\n")
            else:
                arquivo.write("### Estatísticas Descritivas ###\n")
                arquivo.write("Erro: Estatísticas não disponíveis.\n\n")

            if total_vendas_item is not None:
                arquivo.write("### Total de Vendas por Item ###\n")
                arquivo.write(total_vendas_item.to_string())  # Melhor formatação para Series
                arquivo.write("\n")
            else:
                arquivo.write("### Total de Vendas por Item ###\n")
                arquivo.write("Erro: Dados de vendas não disponíveis.\n")

        print(f"Relatório gerado com sucesso: {caminho_arquivo}")
    except Exception as e:
        print(f"Erro ao gerar o relatório: {e}")

# Exemplo de uso:
# gerar_relatorio_texto(estatisticas, total_vendas_item, 'meu_relatorio.txt')
