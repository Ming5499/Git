from random import choice
from requests import post


def title(page):
  return page['a']['title'].split('(')[0].replace('_', ' ').strip()


def category(name, depth=0):
  url = 'https://tools.wmflabs.org/catscan2/catscan2.php'
  payload = {
    'categories': name,
    'depth': depth,
    'format': 'json',
    'doit': 'Do it!',
  }
  category = post(url, data=payload).json()['*'][0]['a']['*']
  return [title(page) for page in category]


first = category('Italian masculine given names')
last = category('Surnames of Italian origin')
work = category('Organized crime members by role')

for i in range(10):
  print(*map(choice, (first, last, work)), sep=',')