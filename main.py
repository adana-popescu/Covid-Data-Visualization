import requests
import csv
from bs4 import BeautifulSoup

URL = "https://www.worldometers.info/coronavirus/"
response = requests.get(URL).text
soup = BeautifulSoup(response, 'html.parser')

table = soup.find('table', id="main_table_countries_today")

rows = table.find_all('tr')

with open('covid-info.csv', 'w', encoding="UTF-8", newline="") as file:
    writer = csv.writer(file)

    for row in rows:
        count = 0
        cells = row.find_all(['th', 'td'])
        country = []

        for cell in cells:
            cell_text = cell.text.replace("\n", '')
            country.append(cell_text)

            count += 1
            if count == 14:
                break
        if country[0] != "":
            writer.writerow(country)
