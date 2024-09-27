import os
import time
from utilities.customLogger import Log_maker
from pageObjects.Homepage import Homepage


class TestRunning:
    baseURL = "https://www.easemytrip.com/hotels/"
    logger = Log_maker.log_gen()

    def test_allpage(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("Opened the base URL")

        self.driver.maximize_window()
        self.logger.info("Maximized the browser window")

        self.driver.implicitly_wait(10)
        self.logger.info("Set implicit wait for 10 seconds")

        self.hp = Homepage(self.driver)
        self.logger.info("Initialized the Homepage object")

         # Perform actions on the homepage
        self.hp.clickads()
        self.logger.info("Clicked on the ads")
        self.hp.clickSearchcity()
        self.logger.info("Clicked on the search city")
        self.hp.entercity("New Delhi")
        self.logger.info("Entered city: New Delhi")
        self.hp.clickselectcity()
        self.logger.info("Selected the city")
        self.hp.clickcheckin()
        self.logger.info("Clicked on check-in")
        self.hp.clickcheckout()
        self.logger.info("Clicked on check-out")
        self.hp.clickroom()
        self.logger.info("Selected the room")
        self.hp.clicksearch()
        self.logger.info("Performed the search")
        time.sleep(3)



