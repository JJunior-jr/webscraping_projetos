import streamlit as st
import pandas as pd
import sqlite3



#conectar no banco de dados SQLite3

conn=sqlite3.connect("data\mercadolivre.sql")

#Carregar os dados da tabela "notbook" em um Dataframe pandas

df= pd.read_sql_query("SELECT * FROM notbook", conn)

# Fechar a conexão com a banco de dados

conn.close()

#Titulo da aplicação

st.title("Pesquisa de Mercado - Notbooks no Mercado Livre")

# Melhorar o layout com colnas para KPIs

st.subheader("KPIs Principais")
col1, col2, col3= st.columns(3)

#KPI1: Número total de itens

total_itens= df.shape[0]
col1.metric(label="Total de Notbooks", value= total_itens)

#KPI2: Número de marcas únicas

unique_brands= df['brand'].nunique()
col2.metric(label="Marcas Únicas", value= unique_brands)

#KPI3: Preço médio novo (em reais)

average_new_price= df['new_money'].mean()
col3.metric(label= "Preço Médio (R$)", value= f"{average_new_price:.2f}")

#marcas mais frequentes

st.subheader("Marcas mais encontradas")
col1, col2= st.columns([4,2])
top_brands= df["brand"].value_counts().sort_values(ascending= False)
col1.bar_chart(top_brands)
col2.write(top_brands)

#Preço médio por marca

st.subheader("Preço Médio por Marca")
col1, col2= st.columns([4,2])
df_non_zero_prices= df[df['new_money']> 0]
average_price_by_brand= df_non_zero_prices.groupby("brand")["new_money"].mean().sort_values(ascending= False)
col1.bar_chart(average_price_by_brand)
col2.write(average_price_by_brand)


#satisfação média por marca
st.subheader("Satisfação Média por Marca")
col1, col2= st.columns([4,2])
df_non_zero_reviews= df[df['reviews_rating_number']> 0]
satisfaction_by_brand= df_non_zero_reviews.groupby("brand")["reviews_rating_number"].mean().sort_values(ascending= False)
col1.bar_chart(satisfaction_by_brand)
col2.write(satisfaction_by_brand)


 





