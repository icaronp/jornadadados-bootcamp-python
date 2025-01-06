import pandas as pd

import os

import glob

import chardet


def etl_arquivos(caminho: str, file: str='*.csv') -> pd.DataFrame:
    arquivos_csv = glob.glob(os.path.join(caminho, '**', file), recursive=True)
    df_list = []

    for arquivo in arquivos_csv:
        with open(arquivo, 'rb') as f:
            result = chardet.detect(f.read())
            encoding = result['encoding']  
            df = pd.read_csv(arquivo, encoding=encoding, sep=';', decimal=',')
            df_list.append(df)

    df_total = pd.concat(df_list, ignore_index=True)
    return df_total

if __name__ == "__main__":
    caminho: str = r"C:\Users\icaro\OneDrive\ENDOVIDA\CONTABILIDADE\DATABASE\STONE"
    print(etl_arquivos(caminho=caminho, encoding='ISO-8859-1'))

# python etl_extract.py

# poetry run python etl_extract.py