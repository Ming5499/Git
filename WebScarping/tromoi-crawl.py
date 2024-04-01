import pandas as pd
import requests
from bs4 import BeautifulSoup

data = []
pages = 1

for page in range(pages, pages+50):  
    url = f'https://tromoi.com/danh-sach?page={page}&province_code=toan-quoc&type=cho-thue-tro'
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')

    container = soup.find('div', class_='modulecontent')
    items = container.find_all('div', class_='item vip column')

    if not items:
        items = container.find_all('div', class_='item hot column')
    
    if not items:
        items = container.find_all('div', class_='item column')

    # Image
    image_urls = []
    for item in items:
        image_tag = item.find('a', style=True)
        if image_tag:
            style_attribute = image_tag['style']
            start_index = style_attribute.index("('") + 2
            end_index = style_attribute.index("')")
            image_url = style_attribute[start_index:end_index]
            image_urls.append(image_url)
        else:
            image_urls.append(None)

    # Info
    for i, item in enumerate(items):
        title = item['title']
        local = item.find('span', class_='local').text.strip().replace(' ', '')
        address = item.find('dl', class_='address').text.strip().replace(' ', '')
        price = item.find('div', class_='price').text.strip().replace(' ', '')
        published = item.find('span', class_='published').text.strip().replace(' ', '')

        data.append({
            'Title': title,
            'Location': local,
            'Address': address,
            'Price': price,
            'Published': published,
            'Image': image_urls[i] if i < len(image_urls) else None  
        })

df = pd.DataFrame(data)
df.to_csv('tromoi.csv', encoding='utf-8', index=False)
