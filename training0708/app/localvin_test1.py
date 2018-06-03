from selenium.webdriver.common.by import By
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class localvin_query(unittest.TestCase):

    def setUp(self):
        TW_INT1 = "http://www-int1.audatex.sg/casemanager"
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages","zh-tw")
        self.driver = webdriver.Firefox(firefox_profile=fp)
        self.driver.get(TW_INT1)
        print(self.driver.title)
        getelement = self.driver.find_element_by_id("ssousername")
        getelement.send_keys("localvin.tw")
        getelement = self.driver.find_element_by_id("password")
        getelement.send_keys("audatex")
        # getelement.submit()
        getelement.send_keys(Keys.RETURN)

        #create new case
        # getelement = self.driver.find_element_by_id("caseData2")
        # getelement.click()
        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME,"claimNumber")))
        # getelement = self.driver.find_element_by_name("claimNumber")
        # getelement.send_keys("claim5")
        # select = Select(self.driver.find_element_by_id("manufacturerCode"))
        # select.select_by_value("47")
        # getelement=self.driver.find_element_by_id("okButton")
        # getelement.click()
        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID,"VehicleIdentification")))

        #Open existing case
        getelement = self.driver.find_element_by_id("tabButton0")
        getelement.click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID,"caseData2")))
        getelement = self.driver.find_element_by_id("showSearch")
        getelement.click()
        getelement = self.driver.find_element_by_id("clearFilter")
        getelement.click()
        getelement = self.driver.find_element_by_id("filter.caseNumber")
        getelement.send_keys("claim6")
        getelement = self.driver.find_element_by_id("button")
        getelement.click()
        WebDriverWait(self.driver,2)
        getelement = self.driver.find_element_by_id("openTask_claim6")
        getelement.click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID,"VehicleIdentification")))

        #Go to Vehicle identification page
        getelement=self.driver.find_element_by_id("VehicleIdentification")
        getelement.click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID,"vehicle.vehicleIdentification.VIN")))

    def test_type3_infiniti(self):
        getelement = self.driver.find_element_by_id("action.clear.all")
        getelement.click()
        WebDriverWait(self.driver,2)
        getelement=self.driver.find_element_by_id("vehicle.vehicleIdentification.VIN")
        getelement.send_keys("JN8CS1MW3EM370102")
        getelement=self.driver.find_element_by_id("vinOk")
        getelement.click()
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,"vehicle.vehicleIdentification.subModelCodeAX")))




    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()