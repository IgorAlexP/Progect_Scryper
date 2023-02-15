import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://service.gadgetufa.ru/')
time.sleep(5)

# Click the 'Ремонт Samsung' link
search_box = driver.find_element(By.LINK_TEXT, 'Ремонт Samsung')
search_box.click()
time.sleep(5)

# Perform a search
"""search_input = driver.find_element(By.NAME, 'q')
search_input.send_keys('Samsung Galaxy A')
search_input.send_keys(Keys.RETURN)
time.sleep(5)"""

# Click the 'Ремонт Galaxy M' link using the PARTIAL_LINK_TEXT locator
search_box = driver.find_element(By.LINK_TEXT, 'Samsung Galaxy A')
search_box.click()
time.sleep(5)

search_box = driver.find_element(By.LINK_TEXT, 'Ремонт Galaxy A51 (2019) SM-A515F')
search_box.click()
time.sleep(10)

driver.quit()
