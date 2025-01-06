import pandas as pd

import os

import glob

import chardet


caminho: str = r"C:\Users\icaro\OneDrive\ENDOVIDA\CONTABILIDADE\DATABASE\STONE\2023\stone_vendas_2022_09.csv"

arquivos_csv = glob.glob(os.path.join(caminho, '*.csv'))

with open(caminho, 'rb') as f:
    result = chardet.detect(f.read())

df = pd.read_csv(caminho, encoding=result['encoding'], sep=';')

print(result)

print(df)

# encoding='ISO-8859-1'

# encoding='latin-1'

# encoding='utf-8'

# encoding='UTF-8-SIG'

# encoding='65001'

# python teste1.py

# poetry run python exercicio-2.py