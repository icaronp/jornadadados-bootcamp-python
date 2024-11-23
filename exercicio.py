import pandas as pd

import csv

import os

import glob

caminho: str = r"C:\Users\icaro\OneDrive\ENDOVIDA\CONTABILIDADE\DATABASE\STONE\2023\stone_vendas_2024_06.csv"

# encoding='ISO-8859-1'
# encoding='latin-1'
# encoding='utf-8'

arquivo_csv: list = []

with open(file=caminho, mode="r") as arquivo:
    leitor_csv = csv.DictReader(arquivo)

    for linha in leitor_csv:
        arquivo_csv.append(linha)


print(arquivo_csv)

# python exercicio.py
