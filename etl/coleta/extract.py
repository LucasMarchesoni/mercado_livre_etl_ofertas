from bs4 import BeautifulSoup
import requests
import time

class Extract():
  def __init__(self, url):
    self.url = url
    self.soup = self.get_html()

  def get_html(self):
    response = requests.get(self.url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup
  
  def get_products(self):
    data = []
    next_page_link = self.soup.find_all("li", class_="andes-pagination__button")[1:-1]
    for next_page_link in next_page_link:
      next_page_url = next_page_link.find('a', class_='andes-pagination__link')
      if next_page_url:
        products = self.soup.find("ol", attrs={"class":"items_container"})
        list_products = products.find_all("li")
        next_page_href = next_page_url.get('href')
        self.url = next_page_href
        self.soup = self.get_html()
        print(f"Coletando produtos da página: {next_page_href}")
        data.append({
          'list_products': list_products
        })
        time.sleep(5)
    else:
      print('Não há mais páginas para coletar')
    return data
  
  def get_products_categories(self):
    products_categories = self.soup.find_all("ol", class_="list")
    return products_categories[1]