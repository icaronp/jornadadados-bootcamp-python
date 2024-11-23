import pandas as pd

import os

import glob

import chardet


caminho: str = r"C:\Users\icaro\OneDrive\ENDOVIDA\CONTABILIDADE\DATABASE\STONE\2024\stone_vendas_2024_07.csv"

arquivos_csv = glob.glob(os.path.join(caminho, '*.csv'))

with open(caminho, 'rb') as f:
    result = chardet.detect(f.read())

df = pd.read_csv(caminho, encoding=result['encoding'])

print(result)

# encoding='ISO-8859-1'

# encoding='latin-1'

# encoding='utf-8'

# 'encoding': 'UTF-8-SIG'

# python teste.py