from selenium.webdriver.common.by import By


class Listingpage():
    Popularity_filter_Xpath = '//*[@id="drpSortFilter"]'
    Lowtohigh_filter_Xpath = '//*[@id="drpItem"]/ul/li[2]/label'
    Login_check_Xpath = '//*[@id="hotelListDiv"]/div/div[4]/div[1]/div[2]/div/div[2]/div[2]/div[11]/span[2]'
    Close_login_Xpath = '//*[@id="lgnBox"]/div[1]/div[1]/div[2]'
    View_room_Xpath = '//*[@id="hotelListDiv"]/div/div[4]/div[4]/div[2]/div/div[2]/div[2]/a/div'

    def __init__(self,driver):
        self.driver = driver


    def clickpopularfilter(self):
        self.driver.find_element(By.XPATH, self.Popularity_filter_Xpath).click()

    def clicklowtohigh(self):
        self.driver.find_element(By.XPATH, self.Lowtohigh_filter_Xpath).click()

    def clicklogin(self):
        self.driver.find_element(By.XPATH, self.Login_check_Xpath).click()

    def clickcloselogin(self):
        self.driver.find_element(By.XPATH, self.Close_login_Xpath).click()

    def clickviewroom(self):
        self.driver.find_element(By.XPATH, self.View_room_Xpath).click()

