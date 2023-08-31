import requests
from bs4 import BeautifulSoup

def crawl_data(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')
  products = soup.find_all('div', class_='product-item')
  for product in products:
    title = product.find('h3', class_='product-name').text
    image_url = product.find('img')['src']
    price = product.find('p', class_='product-price').text
    print(title, image_url, price)

if __name__ == '__main__':
  crawl_data('https://www.thegioididong.com/')