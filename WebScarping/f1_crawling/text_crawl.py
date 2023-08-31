import requests
from bs4 import BeautifulSoup

url = "https://www.formula1.com/en/results.html/2023/drivers.html"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table', {'class': 'resultsarchive-table'})

rows = table.find_all('tr')[1:]

for row in rows:
    columns = row.find_all('td')

    position = columns[1].text.strip()  # Updated column index for position
    driver_name = columns[2].text.strip()
    nationality = columns[3].text.strip()
    team = columns[4].text.strip()
    car = columns[5].text.strip()
    points = columns[6].text.strip()  # Updated column index for points

    print("Position:", position)
    print("Driver:", driver_name)
    print("Nationality:", nationality)
    print("Team:", team)
    print("Car:", car)
    print("Points:", points)
    print("------------------------------------")