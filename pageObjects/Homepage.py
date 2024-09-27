from typing import Tuple

from selenium.webdriver.common.by import By
import os


class Homepage():
    Ads_page_Xpath = '//*[@id="login_pp"]/div/a'
    Searchcity_page_Xpath = "/html/body/div[5]/div/div[3]/div/form/div/div[2]"
    Entercity_section_Xpath = '//*[@id="txtCity"]'
    Select_city_Xpath = '//*[@id="ui-id-1"]/li[1]'
    checkin_section_Xpath = '//*[@id="ui-datepicker-div"]/div[2]/table/tbody/tr[5]/td[4]'
    checkout_section_Xpath = '//*[@id="ui-datepicker-div"]/div[1]/table/tbody/tr[5]/td[5]'
    Room_section_Xpath = '//*[@id="exithotelroom"]'
    Search_section_Xpath = '//*[@id="btnSearch"]'

    def __init__(self, driver):
        self.driver = driver

    def clickads(self):
        self.driver.find_element(By.XPATH, self.Ads_page_Xpath).click()

    def clickSearchcity(self):
        self.driver.find_element(By.XPATH, self.Searchcity_page_Xpath).click()

    def entercity(self, enterlocation):
        self.driver.find_element(By.XPATH, self.Entercity_section_Xpath).send_keys(enterlocation)

    def clickselectcity(self):
        self.driver.find_element(By.XPATH, self.Select_city_Xpath).click()

    def clickcheckin(self):
        self.driver.find_element(By.XPATH, self.checkin_section_Xpath).click()

    def clickcheckout(self):
        self.driver.find_element(By.XPATH, self.checkout_section_Xpath).click()

    def clickroom(self):
        self.driver.find_element(By.XPATH, self.Room_section_Xpath).click()

    def clicksearch(self):
        self.driver.find_element(By.XPATH, self.Search_section_Xpath).click()


