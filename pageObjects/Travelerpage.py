from selenium.webdriver.common.by import By


class TravellerPage():
    CancellationPolicy_Xpath = ""
    signin_Xpath = ""
    CloseSign_Xpath = ""
    ClearPromo_Xpath = ""
    ApplyPromo_Xpath = ""
    FirstName_Xpath = ""
    LastName_Xpath = ""
    EmailId_Xpath = ""
    MobileNo_Xpath = ""
    UncheckTC_Xpath = ""
    checkTC_Xpath = ""
    continue_Xpath = ""

    def __init__(self,driver):
        self.driver=driver

    def checkcancellationpoilcy(self):
        self.driver.find_element(By.XPATH,self.CancellationPolicy_Xpath).click()






