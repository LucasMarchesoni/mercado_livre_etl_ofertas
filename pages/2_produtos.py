import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

conn = sqlite3.connect('data/mercado_livre.db')

df_products = pd.read_sql_query("SELECT * FROM products", conn)

df_products['datetime'] = pd.to_datetime(df_products['datetime'])
last_update_date = df_products['datetime'].max()
last_update_date = last_update_date.strftime("%d/%m/%Y %H:%M:%S")

df_products['new_amount'] = pd.to_numeric(df_products['new_amount'], errors='coerce')
df_products['discount_percent'] = pd.to_numeric(df_products['discount_percent'], errors='coerce')
df_products['total_installments'] = pd.to_numeric(df_products['total_installments'], errors='coerce')
df_products['installments_amount'] = pd.to_numeric(df_products['installments_amount'], errors='coerce')
df_products['original_amount'] = pd.to_numeric(df_products['original_amount'], errors='coerce')

st.title('Produtos')
st.write(f"Última atualização: {last_update_date}")

st.sidebar.markdown("Desenvolvido por [Lucas Marchesoni](https://www.linkedin.com/in/lucasmarchesoni/)")

selected_date = st.selectbox("Selecione a data", sorted(df_products['datetime'].unique().strftime("%d/%m/%Y"), reverse=True))
selected_date = pd.to_datetime(selected_date, format="%d/%m/%Y")
df_products = df_products[df_products['datetime'].dt.date == selected_date.date()]

st.markdown("## **Principais indicadores**")

total_items, max_price, min_price = st.columns(3)

total_items.write(f'**Total de ofertas:** {df_products.shape[0]}')
max_price.write(f'**Preço máximo:** R${df_products["new_amount"].max()}.00')
min_price.write(f'**Preço mínimo:** R${df_products["new_amount"].min()}.00')

mean_discount, mean_installments, mean_installments_amount = st.columns(3)

mean_discount.write(f'**Média desconto:** {format(df_products["discount_percent"].mean(), ".2f")}%')
mean_installments.write(f'**Média parcelas:** {format(df_products["total_installments"].mean(), ".2f")}')
mean_installments_amount.write(f'**Média valor parcela:** R${format(df_products["installments_amount"].mean(), ".2f")}')

st.write("## **Distribuição dos preços**")

boxplot_price = px.box(df_products, y='new_amount', title='Boxplot do preço', labels={'new_amount': 'Valores'})
st.plotly_chart(boxplot_price)

st.write("## **Distribuição dos descontos**")

hist_discounts = px.histogram(df_products, x='discount_percent', title='Histograma dos descontos', labels={'discount_percent': 'Desconto'})
st.plotly_chart(hist_discounts)

st.write("## **Distribuição das parcelas**")

hist_installments = px.histogram(df_products, x='total_installments', title='Histograma das parcelas', labels={'total_installments': 'Parcelas'})
st.plotly_chart(hist_installments)

st.write("## **Total de produtos por fornecedor**")

df_products_per_supplier = df_products.groupby('supplier').size().reset_index(name='count')
df_products_per_supplier = df_products_per_supplier[df_products_per_supplier['count'] > 5]

products_per_supplier = px.bar(df_products_per_supplier, x='supplier', y='count', title='Produtos por fornecedores')
st.plotly_chart(products_per_supplier)

st.write("## **Total por tipos de descontos**")

df_products_per_discount_type = df_products.groupby('discount_type').size().reset_index(name='count')

products_per_discount_type = px.bar(df_products_per_discount_type, x='discount_type', y='count', title='Produtos por fornecedores')
st.plotly_chart(products_per_discount_type)

st.write("## **Card dos produtos**")
st.write("Nessa seção pode-se verificar todas informações referentes aos produtos individualmente")

product = st.selectbox("Selecione um produto", df_products['product_name'])

selected_product_data = df_products[df_products['product_name'] == product].iloc[0]

html_code = f"""
<div class="card" style="padding: 10px; border: 1px solid #ccc; border-radius: 5px; margin-bottom: 20px;">
    <h3 style="margin-bottom: 10px;">{selected_product_data['product_name']}</h3>
    <img src="{selected_product_data['image_url']}" alt="Imagem do Produto" style="width: 200px; margin-bottom: 10px;">
    <p style="margin-bottom: 5px;"><strong>Preço Atual:</strong> {selected_product_data['current_currency']} {selected_product_data['new_amount']}</p>
    <p style="margin-bottom: 5px;"><strong>Preço Original:</strong> {selected_product_data['current_currency']} {selected_product_data['original_amount']}</p>
    <p style="margin-bottom: 5px;"><strong>Desconto:</strong> {selected_product_data['discount_percent']}%</p>
    <p style="margin-bottom: 5px;"><strong>Número de Parcelas:</strong> {selected_product_data['total_installments']}x de {selected_product_data['installments_amount']} {selected_product_data['current_currency']}</p>
    <p style="margin-bottom: 5px;"><strong>Entrega:</strong> {selected_product_data['delivery']}</p>
    <p style="margin-bottom: 5px;"><strong>Fornecedor:</strong> {selected_product_data['supplier']}</p>
    <a href='{selected_product_data['product_link']}' style="margin-bottom: 5px;" target='_blank'><strong>Clique para ir para a página do produto</strong></p>
</div>
"""

st.markdown(html_code, unsafe_allow_html=True)
