import pandas as pd

def calcular_estatisticas_descritivas(df):
    """
    Calcula estatísticas descritivas para um DataFrame.

    Args:
        df (pandas.DataFrame): DataFrame com os dados.

    Returns:
        pandas.DataFrame: DataFrame com as estatísticas descritivas, ou None em caso de erro.
    """
    try:
        if df.empty:
            print("Erro: O DataFrame está vazio.")
            return None

        # Garantir que existem colunas numéricas antes de chamar describe()
        colunas_numericas = df.select_dtypes(include=['number'])
        if colunas_numericas.empty:
            print("Erro: O DataFrame não contém colunas numéricas para análise.")
            return None
        
        # Calcula as estatísticas descritivas sem o argumento numeric_only
        estatisticas = colunas_numericas.describe().copy()
        return estatisticas
    except Exception as e:
        print(f"Ocorreu um erro ao calcular estatísticas: {e}")
        return None

def calcular_total_vendas_por_item(df):
    """
    Calcula o total de vendas por item.

    Args:
        df (pandas.DataFrame): DataFrame com os dados.

    Returns:
        pandas.Series: Series com o total de vendas por item, ou None em caso de erro.
    """
    try:
        colunas_necessarias = {'Item', 'Unidades'}
        colunas_presentes = set(df.columns)

        if not colunas_necessarias.issubset(colunas_presentes):
            colunas_faltando = colunas_necessarias - colunas_presentes
            print(f"Erro: O DataFrame está sem as colunas obrigatórias: {colunas_faltando}.")
            return None

        total_vendas = df.groupby('Item')['Unidades'].sum().copy()
        return total_vendas
    except Exception as e:
        print(f"Ocorreu um erro ao calcular total de vendas: {e}")
        return None
