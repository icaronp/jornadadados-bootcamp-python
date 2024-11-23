import pandas as pd

import os

import glob


caminho = r"C:\Users\icaro\OneDrive\ENDOVIDA\CONTABILIDADE\DATABASE\STONE\2023"

# Função para ler um arquivo CSV com tratamento de erros
def ler_csv(arquivo):
    try:
        # Tentar diversos encodings comuns
        encodings = ['ISO-8859-1', 'latin1', 'utf-8', 'cp1252']
        for encoding in encodings:
            try:
                df = pd.read_csv(arquivo, encoding=encoding, sep=';')
                return df
            except UnicodeDecodeError:
                pass  # Tentar o próximo encoding
        # Se nenhum encoding funcionar, levantar um erro
        raise ValueError(f"Não foi possível encontrar o encoding correto para o arquivo {arquivo}")
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {arquivo}")
        return None

# Ler todos os arquivos CSV no diretório e armazenar em uma lista
arquivos_csv = glob.glob(os.path.join(caminho, '*.csv'))
df_list = [ler_csv(arquivo) for arquivo in arquivos_csv if ler_csv(arquivo) is not None]

print(df_list)