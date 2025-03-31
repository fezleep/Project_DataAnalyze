def formatar_numero(numero, casas_decimais=2):
    """
    Formata um número com um número específico de casas decimais.

    Args:
        numero (float ou int): Número a ser formatado.
        casas_decimais (int, opcional): Número de casas decimais. Padrão é 2.

    Returns:
        str: Número formatado.
    """
    if not isinstance(numero, (float, int)):
        raise ValueError("O parâmetro 'numero' deve ser um número (float ou int).")
    
    if not isinstance(casas_decimais, int) or casas_decimais < 0:
        raise ValueError("O parâmetro 'casas_decimais' deve ser um número inteiro não negativo.")
    
    return f"{numero:.{casas_decimais}f}"

# Exemplo de uso:
# numero_formatado = formatar_numero(1234.5678)
# print(numero_formatado)