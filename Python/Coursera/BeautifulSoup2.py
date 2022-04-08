import urllib.request as ur
from bs4 import *

url = input('Enter the url to scrape - ')

html = ur.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

count_of_spans = 1
sum = 0

spans = soup('span')
for span in spans:
    sum += int(span.contents[0])
    count_of_spans += 1

print('Count ', count_of_spans)
print('Sum ', sum)

##################################################################
current_repeat_count = 0
url = input('Enter URL: ')
repeat_count = int(input('Enter count: '))
position = int(input('Enter position: '))


def parse_html(url):
    html = ur.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    return tags

while current_repeat_count < repeat_count:
    print('Retrieving: ', url)
    tags = parse_html(url)
    for index, item in enumerate(tags):
        if index == position - 1:
            url = item.get('href', None)
            name = item.contents[0]
            break
        else:
            continue
    current_repeat_count += 1
print('Last Url: ', url)