from selenium.webdriver.common.by import By


class Detailpage():
    Detail_login_Xpath = '//*[@id="imageLoginBox"]/img'
    Close_login_Xpath = '//*[@id="lgnBox"]/div[1]/div[1]/div[2]'
    Select_room_Xpath = '/html/body/div[1]/div[8]/div[1]/div[1]/div[3]/div[2]/div[2]/div[4]/a[1]'
    Book_now_Xpath = '//*[@id="availbtn0_0"]/a'


    def __init__(self,driver):
        self.driver=driver


    def clickDetaillogin(self):
        self.driver.find_element(By.XPATH, self.Detail_login_Xpath).click()

    def clickCloselogin(self):
        self.driver.find_element(By.XPATH, self.Close_login_Xpath).click()

    def clickselectroom(self):
        self.driver.find_element(By.XPATH, self.Select_room_Xpath).click()

    def clickbooknow(self):
        self.driver.find_element(By.XPATH, self.Book_now_Xpath).click()



