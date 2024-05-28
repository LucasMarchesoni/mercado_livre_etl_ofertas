from coleta.extract import Extract
from tratamento.transform import Transform
from carregar.load import Load

URL = f'https://www.mercadolivre.com.br/ofertas?container_id=MLB779362-1'

extract = Extract(URL)
list_products = extract.get_products()
products_categories = extract.get_products_categories()

transform = Transform(list_products, products_categories)
transform.save_on_dataframe()
transform.save_on_dataframe_categories()
products = transform.get_dataframe_transformed('products')
categories = transform.get_dataframe_transformed('categories')

load = Load('data/mercado_livre.db')
load.to_sqlite(products, 'products')
load.to_sqlite(categories, 'categories')