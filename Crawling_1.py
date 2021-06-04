from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get(주소)
elem = driver.find_element_by_name("q")
elem.send_keys("key")
elem.send_keys(Keys.RETURN)
driver.find_
