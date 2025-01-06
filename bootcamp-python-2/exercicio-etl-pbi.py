import pandas as pd
import glob
import os


def etl_arquivos(caminho: str, encoding: str='utf-8', file: str='*.csv') -> pd.DataFrame:
    arquivos_csv = glob.glob(os.path.join(caminho, '**', file), recursive=True)
    df_list = [pd.read_csv(arquivo, encoding=encoding, sep=';', decimal=',') for arquivo in arquivos_csv]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total

def remover_colunas(df: pd.DataFrame, lista_colunas: list) -> pd.DataFrame:
    return df.drop(lista_colunas, axis=1)


def unificar_colunas(df: pd.DataFrame, lista_com_colunas_em_tuplas: list) -> pd.DataFrame:
    for coluna1, coluna2 in lista_com_colunas_em_tuplas:
        df[coluna1] = df[coluna1].fillna(df[coluna2])
        df.drop(coluna2, axis=1, inplace=True)
    return df


def renomear_colunas(df: pd.DataFrame, dict_colunas_novo_nome: dict) -> pd.DataFrame:
    df = df.rename(columns=dict_colunas_novo_nome)
    return df


def substituir_valores(df: pd.DataFrame, dict_colunas_substituicoes: dict) -> pd.DataFrame:
    """
    Substitui valores em múltiplas colunas de um DataFrame, com dicionários de substituições personalizados para cada coluna.

    Args:
        df: O DataFrame a ser modificado.
        dict_colunas_substituicoes: Um dicionário onde as chaves são os nomes das colunas e os valores são dicionários de substituições.

    Returns:
        O DataFrame com as substituições realizadas.
    """

    for coluna, substituicoes in dict_colunas_substituicoes.items():
        df[coluna] = df[coluna].replace(substituicoes)
    return df


def preencher_vazias(df: pd.DataFrame, dict_colunas_valores: dict) -> pd.DataFrame:
    df = df.fillna(value=dict_colunas_valores)
    """values = {{"A": 0, "B": 1, "C": 2, "D": 3}}"""
    return df


if __name__ == "__main__":

    import time

    print("Iniciando o processamento do arquivo.")
    start_time = time.time()

    caminho: str = r"C:\Users\icaro\OneDrive\ENDOVIDA\CONTABILIDADE\DATABASE\STONE"

    df_extraido = etl_arquivos(caminho=caminho, encoding='ISO-8859-1')

    df_transform = remover_colunas(df=df_extraido, lista_colunas=['STONE ID', 'STONECODE', 'BANDEIRA', 'ÚLTIMO STATUS', 
                                                                     'SERIAL NUMBER', 'NÚMERO DE SÉRIE', 'N° CARTÃO', 
                                                                     'DATA DO ÚLTIMO STATUS', 'STONE CODE'])
    
    df_transform = renomear_colunas(df_transform, {'TIPO': 'FORMA DE PAGTO'})


    df_transform = unificar_colunas(df_transform, [('FORMA DE PAGTO', 'PRODUTO'),
                                                       ('DATA DA VENDA', 'HORA DA VENDA')])
    
    df_transform = substituir_valores(df_transform, {'FORMA DE PAGTO': {'Débito': 'Débito 1x', 
                                                                        'Débito Pré-pago': 'Débito 1x',
                                                                        'Crédito Pré-pago': 'Crédito 1x',
                                                                        'Crédito': 'Crédito 1x'}}) 
    
    df_transform = preencher_vazias(df_transform, {'DESCONTO DE ANTECIPAÇÃO': 0, 
                                                   'DESCONTO DE MDR': df_transform['VALOR BRUTO'].astype(float) - df_transform['VALOR LÍQUIDO'].astype(float),
                                                   'QTD DE PARCELAS': df_transform['FORMA DE PAGTO'].str.split(' ').str[-1].str[:-1].astype(float)})

    
    df_transform['QTD DE PARCELAS'] = df_transform['QTD DE PARCELAS'].astype(int)
    
    print(df_transform)   
  
    took = time.time() - start_time

    print(f"Processing took: {took:.2f} sec")

    # poetry run python etl_powerbi_teste.py