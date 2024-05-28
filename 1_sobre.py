import streamlit as st
import sqlite3
import pandas as pd
import webbrowser

conn = sqlite3.connect('data/mercado_livre.db')

df_products = pd.read_sql_query("SELECT * FROM products", conn)

df_products['datetime'] = pd.to_datetime(df_products['datetime'])
last_update_date = df_products['datetime'].max()
last_update_date = last_update_date.strftime("%d/%m/%Y %H:%M:%S")

st.title('Pesquisa de mercado - Ofertas do Mercado Livre')
st.write(f"Última atualização: {last_update_date}")

st.sidebar.markdown("Desenvolvido por [Lucas Marchesoni](https://www.linkedin.com/in/lucasmarchesoni/)")

st.markdown("""
  Os dados foram retirados da página de ofertas do site de comercio digital mercado livre. O conjunto de dados foi dividido em duas tabelas, produtos e categoria.
            
  Na tabela de produtos possui informações como sua imagem, o link de acesso, o preço, descontos, etc. Na tabela de categorias possui informações como link de acesso para aquele filtro, total de itens e o título da categoria.
""")

btn_mercado_livre = st.button("Acesse a página com os dados")
if btn_mercado_livre:
  webbrowser.open_new_tab("https://www.mercadolivre.com.br/ofertas?container_id=MLB779362-1")

st.markdown("""
  ## Utilização do dashboard
  
  - Produtos: Análise gráfica dos produtos;
  - Categorias: Disponibilização do acesso para cada categoria;
  
  ## Atualização dos dados

  Os dados são atualizados 1x por dia.
  
  ## Ferramentas
            
  - **Python**: Linguagem utilizada no projeto.
  - **Beautiful Soup**: Biblioteca para realizar do webscraping.
  - **Pandas**: Biblioteca utilizada para tratamento e manipulação da base.
  - **Streamlit**: Biblioteca utilizada para desenvolvimento do dashboard.
  - **SQLite**: Banco de dados utilizado para armazenamento dos dados.
  - **Github Actions**: Automação do ETL do projeto.
            
  ## Redes sociais
  - Linkedin: https://www.linkedin.com/in/lucasmarchesoni/
  - Repositório do projeto: https://github.com/LucasMarchesoni/mercado_livre_etl_ofertas
  - Github: https://github.com/LucasMarchesoni
""")