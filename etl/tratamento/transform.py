import pandas as pd
from datetime import datetime
import re

class Transform():
  def __init__(self, list_products, products_categories):
    self.list_products = list_products
    self.products_categories = products_categories
    self.df = self.create_dataframe()
    self.df_categories = self.create_dataframe()

  def create_dataframe(self):
    return pd.DataFrame()
  
  def save_on_dataframe(self):
    data = []
    datetime_now = datetime.now()
    for list_products in self.list_products:
      list_products = list_products['list_products']
      for product in list_products:
        img_tag = product.find('img', class_='promotion-item__img')
        if img_tag: 
          image_url = img_tag.get('src')
        else:
          image_url = None

        link = product.find('a', class_="promotion-item__link-container")
        if link:
          product_link = link.get("href")
        else:
          product_link = None

        title = product.find('p', class_="promotion-item__title")   
        if title:
          product_name = title.get_text()
        else:
          product_name = None

        currency = product.find('span', class_="andes-money-amount__currency-symbol")
        if currency:
          current_currency = currency.get_text()
        else:
          current_currency = None

        total_amount = product.find('span', class_="andes-money-amount__fraction")
        if total_amount:
          new_amount = total_amount.get_text().replace(".", "")
        else:
          new_amount = None
        
        discount_div = product.find('s', class_="andes-money-amount andes-money-amount-combo__previous-value andes-money-amount--previous andes-money-amount--cents-superscript")
        if discount_div:
          total_original_amount = discount_div.find('span', class_="andes-money-amount__fraction")
          if total_original_amount:
            original_amount = total_original_amount.get_text().replace(".", "")
          else:
            original_amount = new_amount
        
        discount = product.find('span', class_='promotion-item__discount-text')
        if discount:
          discount_value = re.search(r'(\d+)% OFF', discount.get_text())

          if discount_value:
            discount_percent = discount_value.group(1)
          else:
            discount_percent = 0

        total_installments = None
        installments_tag = product.find('span', class_='promotion-item__installments')
        if installments_tag:
          installments_text = installments_tag.get_text(strip=True)
          match = re.search(r'(\d+)x', installments_text)
          if match:
              total_installments = int(match.group(1))
              installments_amount = int(new_amount) / total_installments
          else:
            installments_amount = None
            total_installments = None
        else:
            installments_amount = None
            total_installments = None

        delivery_tag = product.find('span', class_='promotion-item__pill')
        if delivery_tag:
          delivery = delivery_tag.get_text()
        else:
          delivery = None

        supplier_tag = product.find('span', class_="promotion-item__seller")
        if supplier_tag:
          supplier = supplier_tag.get_text()
        else:
          supplier = None

        discount_tag = product.find('span', class_='rebates_discount_pill new_pills')
        if discount_tag:
          discount_type = discount_tag.get_text()
        else:
          discount_type = None

        data.append({
              'image_url': image_url,
              'product_link': product_link,
              'product_name': product_name,
              'current_currency': current_currency,
              'new_amount': new_amount,
              'original_amount': original_amount,
              'discount_percent': discount_percent,
              'discount_type': discount_type,
              'total_installments': total_installments,
              'installments_amount': installments_amount,
              'delivery': delivery,
              'supplier': supplier,
              'datetime': datetime_now 
          })

      self.df = pd.DataFrame(data)

  def save_on_dataframe_categories(self):
    data = []
    for category in self.products_categories:
      link_tag = category.find("a", class_="list_element")
      if link_tag:
        link = link_tag.get('href')
      else:
        link = None

      category_title_raw = category.text.strip()
      category_title, quantity_raw = category_title_raw.split('(')
      category_title = category_title.strip()
      quantity = quantity_raw.replace(')', '').strip()

      data.append({
        'link': link,
        'category': category_title,
        'quantity': quantity,
        'datetime': datetime.now()
      })

      self.df_categories = pd.DataFrame(data)

  def get_dataframe_transformed(self, type):
    if type == 'products':
      return self.df
    elif type == 'categories':
      return self.df_categories