
import pandas as pd

import os

import glob


caminho: str = r"C:\Users\icaro\OneDrive\ENDOVIDA\CONTABILIDADE\DATABASE\STONE\2023"

arquivos_csv = glob.glob(os.path.join(caminho, '*.csv'))

df_list = [pd.read_csv(arquivo, encoding='ISO-8859-1', sep=';') for arquivo in arquivos_csv]

df_total = pd.concat(df_list, ignore_index=True)

print(df_total)

# encoding='ISO-8859-1'

# encoding='latin-1'

# encoding='utf-8'

# python stone_etl.py
