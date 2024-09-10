from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import pandas as pd
import time

# # URL of the website to scrape
# url = "https://www.instagram.com/cristiano/following/"
url = "https://www.instagram.com/"

service = Service(executable_path=r'/usr/bin/chromedriver')
PROXY = "0.0.0.0" # your proxy here
options = webdriver.ChromeOptions()
options.add_argument('--headless=new')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--proxy-server=%s' % PROXY)
driver = webdriver.Chrome(service=service, options=options)

# find class element follower
# get_following = driver.find_element(By.CLASS_NAME, "x7r02ix xf1ldfh x131esax xdajt7p xxfnqb6 xb88tzc xw2csxc x1odjw0f x5fp0pe")

# get_length_following.click()

# fill q
# q = driver.find_element(By.ID, "q")
# # fill with keyword "kings"
# q.send_keys("kings")
# # submit
# q.submit()

# read current url
time.sleep(5)
driver.get(url)
print(driver.current_url)
print(driver.title)

# login
time.sleep(5)
# username=driver.find_element_by_css_selector("input[name='username']")
username=driver.find_element(By.CSS_SELECTOR, "input[name='username']")
# password=driver.find_element_by_css_selector("input[name='password']")
password=driver.find_element(By.CSS_SELECTOR, "input[name='password']")
username.clear()
password.clear()
username.send_keys("iluania_")
password.send_keys("#qwerty123#")
login = driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


#save your login info?
# time.sleep(10)
# notnow = driver.find_element(By.XPATH, "//div[@role='button']").click()
# # notnow_click = driver.find_element(By.XPATH, "//div[@role='button'] contains(text(), 'Not Now')]").click()
# #turn on notif
# time.sleep(10)
# notnow2 = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()

# time.sleep(3)
# #click on profile page
# get_profile_page = driver.find_element(By.XPATH, "//a[contains(@href, '/{}')]".format(username)).click()
# time.sleep(2)

# read current url
time.sleep(5)
driver.get(url)
print(driver.current_url)
print(driver.title)

# def converting (self, nameList):
#     IGuserName = 5"\n".join(nameList)
#     return IGuserName

# def following_user(self):
#     #click on following button(People you are following; people you like)
#     self.browser.find_element_by_xpath("//a[contains(@href, '/following')]").click()
#     #print(f"{line} click on following !!! {line}")
#     time.sleep(2)
#     # copy the xpath of scrollbar
#     #not working
#     #scroll_box = self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div[3]")
#     scroll_box = self.browser.find_element_by_xpath("//div[@class='isgrP']")
#     time.sleep(5)
#     # height variable
#     last_ht, ht = 0, 1
#     while last_ht != ht:
#         last_ht = ht
#         time.sleep(2)
#         # scroll down and retrun the height of scroll
#         ht = self.browser.execute_script(""" 
#         arguments[0].scrollTo(0, arguments[0].scrollHeight);
#         return arguments[0].scrollHeight; """, scroll_box)
#     # list follower name
#     time.sleep(5)
#     #print(f"{line} Scroll Buttom  Done!!! {line}")
#     links = scroll_box.find_elements_by_tag_name('a')
#     time.sleep(2)
#     names = [name.text for name in links if name.text != '']
#     # need to filter empty string so we used name.text instead of name
#     print(names)
#     #print(f"{line} follower list done!!! {line}")
#     # hit close button
#     #self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div[1]/div/div[2]/button").click()
#     self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[1]/div/div[3]/div/button").click()
#     #print(f"{line} close Follower  Done!!! {line}")

#     #convert list to string
#     converting = self.converting(names)
#     print(f"{line} convert list to string  Done!!! {line}")
#     print(converting)
#     print(f"{line} Printing name  {line}")
#     #self.quiting()

# # read current url
# url2 = "https://www.instagram.com/cristiano/following/"
# time.sleep(5)
# driver.get(url2)
# print(driver.current_url)
# print(driver.title)

# Print all table values
# html_body = driver.find_element(By.XPATH, "//body")
# # take screenshot
# time.sleep(20)
# html_body.screenshot("ss_ig.png")
# driver.save_screenshot('screenshot_ig.png')
# driver.save_screenshot('screenshot.png')
# driver.execute_script("document.body.style.zoom='50%'")

#searchbox
# time.sleep(5)
# searchbox=driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search']")
# searchbox.clear()
# searchbox.send_keys("host.py")
# time.sleep(5)
# searchbox.send_keys(Keys.ENTER)
# time.sleep(5)
# searchbox.send_keys(Keys.ENTER)

driver.quit()