from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

#selection du site web ( ici wikipedia )
url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

#l'agent est obligatoire pour acceder a wikipedia en tant qu'un robot ( le code se comporte comme robot sur le web )
head = {
    "User-Agent": "Mozilla/5.0 (compatible; MyScraper/1.0; +https://example.com/bot)"
}

page = requests.get(url , headers = head)

soupe = BeautifulSoup(page.text ,'html.parser' ) #A WARNING ? attention

tables =  soupe.find_all('table')

# extration des donnes des entreprises et leurs revenues
companies = soupe.find('table' , class_="wikitable sortable")
tbheader = companies.find_all('th')
tbcontent = companies.find_all('tr')

tbheader = [title.text.strip() for title in tbheader]

"""--------DATA SOUS FORME DE LIST ---------------"""
rows = []
for row in tbcontent:
  rows.append([ data.text.strip() for data in row.find_all('td')] )
print(rows)
    #rows.append( row.find_all('td').text.strip() )

df = pd.DataFrame(columns = tbheader)

"""-----------------DATA SOUS FORME D'UN DATAFRAME -----------------"""

for row in tbcontent[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]

    length = len(df)
    df.loc[length] = individual_row_data


#tbcontent = [.text.strip() for data in tbcontent]

print(rows)

print(df)

# convertion en csv pour un autre projet
path = r"C:\Users\fares\Documents\companies.csv"
df.to_csv(path, index=False, encoding='utf-8')


