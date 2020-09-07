import requests
from bs4 import BeautifulSoup
import csv


url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = response.content

soup = BeautifulSoup(html, 'html.parser')
table = soup.find('tbody', attrs={'class': 'lister-list'})


list_of_rows = []
for row in table.findAll('tr'):
	list_of_cells = []
	for cell in row.findAll('td'):
		text = cell.text.replace('&ndsp;','')
		list_of_cells.append(text)
	list_of_rows.append(list_of_cells)


outfile = open('./topmovies.csv', 'w')
writer = csv.writer(outfile)
writer.writerows(list_of_rows)
