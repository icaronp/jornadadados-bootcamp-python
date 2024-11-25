
from etl_extract import etl_arquivos

import pandas as pd

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


if __name__ == "__main__":

    caminho: str = r"C:\Users\icaro\OneDrive\ENDOVIDA\CONTABILIDADE\DATABASE\STONE"

    df_extraido = etl_arquivos(caminho=caminho, encoding='ISO-8859-1')

    df_transform_1 = remover_colunas(df=df_extraido, lista_colunas=['STONE ID', 'STONECODE', 'BANDEIRA', 'ÚLTIMO STATUS', 
                                                                     'SERIAL NUMBER', 'NÚMERO DE SÉRIE', 'N° CARTÃO', 
                                                                     'DATA DO ÚLTIMO STATUS', 'STONE CODE'])
    
    df_transform_2 = renomear_colunas(df_transform_1, {'TIPO': 'FORMA DE PAGTO'})
    #                                                   'HORA DA VENDA': 'DATA DA VENDA',
    #                                                   'TIPO': 'FORMA DE PAGTO', 
    #                                                   'PRODUTO': 'FORMA DE PAGTO'})
    
    df_transform_3 = unificar_colunas(df_transform_2, [('FORMA DE PAGTO', 'PRODUTO'),
                                                       ('DATA DA VENDA', 'HORA DA VENDA')])
    print(df_transform_3)      

# poetry run python etl_extract.py
# poetry run python etl_transform.py