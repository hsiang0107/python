import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
__author__ = 'twlhgs'

# driver = webdriver.Firefox()
# driver.get("https://www-int1.audatex.sg/bre")
# print(driver.title)

project_path = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
print(project_path)
webdriver_path = os.path.join(project_path,'webdriver','chromedriver.exe')
print(webdriver_path)

if __name__ == '__main__':
    chrome_opts = Options()
    chrome_opts.add_argument("--lang=en")
    driver = webdriver.Chrome(webdriver_path,chrome_options=chrome_opts)
    driver.get("https://www-int1.audatex.sg/bre")
    print(driver.title)

    getelement = driver.find_element_by_id("ssousername")
    getelement.send_keys("sean.huang.ga.my")
    getelement = driver.find_element_by_id("password")
    getelement.send_keys("audatex")
    # getelement.submit()
    getelement.send_keys(Keys.RETURN)

    try:
        getelement = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"ui-id-1")))
        getelement = driver.find_element_by_id("BREForm_root.notification.itemCountLoginNotification.itemCountLoginNotificationdialogCancel")
        getelement.click()
    finally:
        pass
    # driver.quit()
