
import pandas as pd

import os

import glob

# encoding='ISO-8859-1'
# encoding='latin-1'
# encoding='utf-8'
# encoding='UTF-8-SIG'
# encoding='65001'

def etl_arquivos(caminho: str, encoding: str='utf-8', file: str='*.csv') -> pd.DataFrame:
    arquivos_csv = glob.glob(os.path.join(caminho, file))
    df_list = [pd.read_csv(arquivo, encoding=encoding, sep=';') for arquivo in arquivos_csv]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total

# python stone_etl.py

# poetry run python stone_etl.py


if __name__ == "__main__":
    caminho: str = r"C:\Users\icaro\OneDrive\ENDOVIDA\CONTABILIDADE\DATABASE\STONE\2023"
    print(etl_arquivos(caminho=caminho, encoding='ISO-8859-1'))
