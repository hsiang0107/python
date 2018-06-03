from selenium.webdriver.common.by import By

__author__ = 'twlhgs'
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

INT1_BRE = "https://www-int1.audatex.sg/bre"
TW_INT1 = "http://www-int1.audatex.sg/casemanager"
fp = webdriver.FirefoxProfile()
fp.set_preference("intl.accept_languages","zh-tw")
driver = webdriver.Firefox(firefox_profile=fp)
driver.get(INT1_BRE)
print(driver.title)
getelement = driver.find_element_by_id("ssousername")
getelement.send_keys("sean.huang.ga.tw")
getelement = driver.find_element_by_id("password")
getelement.send_keys("audatex")
# getelement.submit()
getelement.send_keys(Keys.RETURN)

try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"ui-id-1")))
    getelement = driver.find_element_by_id("BREForm_root.notification.itemCountLoginNotification.itemCountLoginNotificationdialogCancel")
    getelement.click()
finally:
    pass
# driver.quit()
