

import pandas as pd

def carregar_dados_csv(caminho_arquivo, codificacao='utf-8', delimitador=',', header=True):
    """
    Carrega dados de um arquivo CSV.

    Args:
        caminho_arquivo (str): Caminho para o arquivo CSV.
        codificacao (str, opcional): Codificação do arquivo. Padrão é 'utf-8'.
        delimitador (str, opcional): Delimitador do arquivo. Padrão é ','.
        header (bool, opcional): Define se o CSV contém cabeçalho. Padrão é True.

    Returns:
        pandas.DataFrame: DataFrame com os dados do arquivo ou None em caso de erro.
    """
    try:
        df = pd.read_csv(
            caminho_arquivo,
            encoding=codificacao,
            delimiter=delimitador,
            header=0 if header else None  # Define se há cabeçalho ou não
        )
        return df
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado em {caminho_arquivo}. Verifique o caminho.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Erro: O arquivo {caminho_arquivo} está vazio.")
        return None
    except pd.errors.ParserError:
        print(f"Erro: Falha ao processar o arquivo CSV. Verifique se o delimitador '{delimitador}' está correto.")
        return None
    except Exception as e:
        print(f"Ocorreu um erro ao carregar o arquivo {caminho_arquivo}: {e}")
        return None
