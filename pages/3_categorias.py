import streamlit as st
import sqlite3
import pandas as pd

conn = sqlite3.connect('data/mercado_livre.db')

df_category = pd.read_sql_query("SELECT * FROM categories", conn)

df_category['datetime'] = pd.to_datetime(df_category['datetime'])
last_update_date = df_category['datetime'].max()
last_update_date = last_update_date.strftime("%d/%m/%Y %H:%M:%S")

max_date = df_category['datetime'].max()
df_category = df_category[df_category['datetime'].dt.date == max_date.date()]

st.title('Categorias')

st.write(f"Última atualização: {last_update_date}")

st.sidebar.markdown("Desenvolvido por [Lucas Marchesoni](https://www.linkedin.com/in/lucasmarchesoni/)")

st.write("Nessa seção é possível acessar os produtos por cada categoria")

cards_html = ""

for idx, row in df_category.iterrows():
    card_html = f"""
    <div class="card" style="padding: 10px; border: 1px solid #ccc; border-radius: 5px; margin-bottom: 20px;">
        <h3 style="margin-bottom: 10px;">{row['category']}</h3>
        <p style="margin-bottom: 5px;">Quantidade: {row['quantity']}</p>
        <a href="{row['link']}" style="margin-bottom: 5px;" target="_blank"><strong>Ver produtos da categoria</strong></a>
    </div>
    """
    cards_html += card_html

st.markdown(cards_html, unsafe_allow_html=True)
