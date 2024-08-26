import requests

from bs4 import BeautifulSoup
import pandas as pd
import time

# URL of the website to scrape
url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5",
}

# Send an HTTP GET request to the website
# response = requests.get(url, headers=headers)
response = requests.get(url)

# Parse the HTML code using BeautifulSoup
# soup = BeautifulSoup(response.content, 'html.parser')
soup = BeautifulSoup(response.text, 'html')

# table = soup.find_all('table', class_ = 'wikitable sortable')[1]
table = soup.find_all('table')[0]
print("🚀 ~ table:", table)
# print("🚀 ~ soup:", soup)

world_titles = table.find_all('th')
world_table_titles = [title.text.strip() for title in world_titles]
# print("🚀 ~ world_table_titles:", world_table_titles)

# Extract the relevant information from the HTML code
# movies = []
# for row in soup.select('tbody.lister-list tr'):
#     title = row.find('td', class_='titleColumn').find('a').get_text()
#     year = row.find('td', class_='titleColumn').find('span', class_='secondaryInfo').get_text()[1:-1]
#     rating = row.find('td', class_='ratingColumn imdbRating').find('strong').get_text()
#     movies.append([title, year, rating])

# Store the information in a pandas dataframe
df = pd.DataFrame(columns = world_table_titles)
# print("🚀 ~ df:", df)

column_data = table.find_all('tr')

# print("🚀 ~ column_data:", column_data)

for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [ data.text.strip() for data in row_data]
    # print("🚀 ~ individual_row_data:", individual_row_data)
    length = len(df)
    df.loc[length] = individual_row_data
    # df.to_csv('top-valued-companies-usa.csv', index=False)
# print("🚀 ~ df:", df)
    
 

# # Add a delay between requests to avoid overwhelming the website with requests
# time.sleep(1)

# Export the data to a CSV file
df.to_csv('top-valued-companies-usa.csv', index=False)