from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import requests
import pandas as pd
import time

# # URL of the website to scrape
url = "https://www.scrapethissite.com/pages/forms"

service = Service(executable_path=r'/usr/bin/chromedriver')
PROXY = "0.0.0.0" # your proxy here
options = webdriver.ChromeOptions()
options.add_argument('--headless=new')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--proxy-server=%s' % PROXY)
driver = webdriver.Chrome(service=service, options=options)

driver.get(url)
# print(driver.title)

# fill q
q = driver.find_element(By.ID, "q")
# fill with keyword "kings"
q.send_keys("kings")
# submit
q.submit()

# read current url
print(driver.current_url)

# Print all table values
table = driver.find_element(By.CLASS_NAME, "table")
# take screenshot
table.screenshot("table-screenshot.png")
# driver.save_screenshot('screenshot.png')
driver.execute_script("document.body.style.zoom='50%'")
driver.save_screenshot('screenshot.png')
# print(table.text)

driver.quit()

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5",
# }

# # Send an HTTP GET request to the website
# driver = webdriver.Chrome()
# driver.get(url)

# print(driver.title)


# Parse the HTML code using BeautifulSoup
# # soup = BeautifulSoup(response.content, 'html.parser')
# soup = BeautifulSoup(response.text, 'html')

# # table = soup.find_all('table', class_ = 'wikitable sortable')[1]
# table = soup.find_all('table')[0]
# print("🚀 ~ table:", table)
# # print("🚀 ~ soup:", soup)

# world_titles = table.find_all('th')
# world_table_titles = [title.text.strip() for title in world_titles]
# # print("🚀 ~ world_table_titles:", world_table_titles)

# # Extract the relevant information from the HTML code
# # movies = []
# # for row in soup.select('tbody.lister-list tr'):
# #     title = row.find('td', class_='titleColumn').find('a').get_text()
# #     year = row.find('td', class_='titleColumn').find('span', class_='secondaryInfo').get_text()[1:-1]
# #     rating = row.find('td', class_='ratingColumn imdbRating').find('strong').get_text()
# #     movies.append([title, year, rating])

# # Store the information in a pandas dataframe
# df = pd.DataFrame(columns = world_table_titles)
# # print("🚀 ~ df:", df)

# column_data = table.find_all('tr')

# # print("🚀 ~ column_data:", column_data)

# for row in column_data[1:]:
#     row_data = row.find_all('td')
#     individual_row_data = [ data.text.strip() for data in row_data]
#     # print("🚀 ~ individual_row_data:", individual_row_data)
#     length = len(df)
#     df.loc[length] = individual_row_data
#     # df.to_csv('top-valued-companies-usa.csv', index=False)
# # print("🚀 ~ df:", df)
    
 

# # # Add a delay between requests to avoid overwhelming the website with requests
# time.sleep(1)

# # Export the data to a CSV file
# df.to_csv('top-valued-companies-usa.csv', index=False)