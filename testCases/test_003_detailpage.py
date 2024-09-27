import time
from utilities.customLogger import Log_maker
from pageObjects.Detailpage import Detailpage
from selenium.webdriver.chrome.options import Options


class TestDetail:
    baseURL = 'https://www.easemytrip.com/hotels/zip-by-spree-hotels-delhi-greater-kailash-3467732/?e=20249134349&city=New%20Delhi,National%20Capital%20Territory%20Of%20Delhi,India&cin=30/10/2024&cOut=31/10/2024&Hotel=NA&Rooms=1&pax=2&key=15~INR~NEW%20DELHI~10-30-2024~10-31-2024~1~2_~~~EASEMYTRIP~NA~NA~NA~IN&ecid=EMTHOTEL-3467732&hid=36916784'
    logger = Log_maker.log_gen()

    # def disable_chrome_notifications(self):
    #     chrome_options = Options()
    #     chrome_options.add_experimental_option("prefs", {
    #         "profile.default_content_setting_values.notifications": 2  # 1 for allow, 2 for block
    #     })
    def disable_chrome_notifications(self):
        chrome_option = Options()
        chrome_option.add_experimental_option("prefs",{
            "profile.default_content_setting_values.notifications":2
        })



    def test_detailpage(self, setup):

        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("Opening the detailpage base URL")

        self.driver.maximize_window()
        self.logger.info("Max the browser window")

        self.driver.implicitly_wait(10)
        self.logger.info("Adding the wait for 10 sec")

        self.dp = Detailpage(self.driver)
        self.logger.info("Initialized the Detailpage object")

        # Performing the action on the Detail page

        self.dp.clickDetaillogin()
        self.logger.info("Click on Detail page")

        self.dp.clickCloselogin()
        self.logger.info("Click on close login option ")

        self.dp.clickselectroom()
        self.logger.info("Click on select room section ")

        time.sleep(5)

        self.dp.clickbooknow()
        self.logger.info("Click on book now option")
