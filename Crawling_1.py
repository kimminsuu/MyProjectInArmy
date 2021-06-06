from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get(주소)
elem = driver.find_element_by_name("q")
elem.send_keys("key")
elem.send_keys(Keys.RETURN)
driver.find_elements_by_css_selector(".rg_i.Q4LuWd")[0].click()
#이미지 주소로 다운로드 받는다.

#나머지는 구글에서 F12를 눌러 주소를 복사해 넣으며 크롤링하면 됨/
