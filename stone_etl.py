
import pandas as pd

import os

import glob


caminho: str = r"C:\Users\icaro\OneDrive\ENDOVIDA\CONTABILIDADE\DATABASE\STONE\2023"

arquivos_csv = glob.glob(os.path.join(caminho, '*.csv'))

df_list = [pd.read_csv(arquivo, encoding='ISO-8859-1', sep=';') for arquivo in arquivos_csv]

print(df_list)

# encoding='ISO-8859-1'

# encoding='latin-1'

# encoding='utf-8'

# python etl_stone.py
