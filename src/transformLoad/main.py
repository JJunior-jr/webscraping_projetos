import pandas as pd
from datetime import datetime
import sqlite3



# Definir o caminho para o jsonl 

df=  pd.read_json('data\data.jsonl', lines=True)
print(df)

# Setar o pandas para mostar todas as colunas
pd.set_option('display.max_columns', None)
#pd.set_option.display.max_columns= None este é a versão da live

#Adcionar a coluna _source com um valor fixo (neste caso é para saber de qual sistema os dados vieram, isso é importante para o ETL e colocado como padrão)
df['_source'] = 'https://lista.mercadolivre.com.br/notebook'


# adcionar a coluna _data_coleta com a data e hora atual

#df['_data_coleta'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

df['_data_coleta'] = datetime.now()

# Tratar os valores nulor para colunas numéricas e de texto(não foi feito)


# Garantir que estão todos como strings antes de usar o .str
# tirar os pontos (.) por nada e os parenteses () por nada.
df['old_money'] =  df['old_money'].astype(str).str.replace('.','', regex= False)
df['new_money'] =  df['new_money'].astype(str).str.replace('.','', regex= False)
df['reviews_amount'] =  df['reviews_amount'].astype(str).str.replace('[\(\)]', '', regex= True)


# Converter para números

df['old_money'] =  df['old_money'].astype(float)
df['new_money'] =  df['new_money'].astype(float)
df['reviews_rating_number'] =  df['reviews_rating_number'].astype(float)
df['reviews_amount'] =  df['reviews_amount'].astype(int)

#Tratar o s pereços como floats e calcular oas valores totais
#Manter apenas produtos com preço entre 100 e 10000 reais


df= df['_data_coleta'
       (df['old_money'] >= 1000) & (df['old_money'] <= 10000) &
       (df['new_money'] >= 1000) & (df['new_money'] <= 10000)

       ]


print(df)



