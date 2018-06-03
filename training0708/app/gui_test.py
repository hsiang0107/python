__author__ = 'twlhgs'
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://www.google.com")
print(driver.title)
getelement = driver.find_element_by_id("lst-ib")
getelement.send_keys("audatex")
# getelement.submit()
getelement.send_keys(Keys.RETURN)

try:
    WebDriverWait(driver, 10).until(EC.title_contains("audatex"))
    print(driver.title)
finally:
    pass
# driver.quit()
