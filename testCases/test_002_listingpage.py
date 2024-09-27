import time
from utilities.customLogger import Log_maker
from pageObjects.Listingpage import Listingpage


class TestListing():
    baseURL = 'https://www.easemytrip.com/hotels/htl-in-new-delhi/?e=202491215425&city=New%20Delhi,National%20Capital%20Territory%20Of%20Delhi,India&cin=30/10/2024&cOut=31/10/2024&Hotel=NA&Rooms=1&pax=2'
    logger = Log_maker.log_gen()

    def test_listingpage(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("opening the listing page url")

        # performing action on Listing page using try.

        self.driver.maximize_window()
        self.logger.info("max the browser window")

        self.driver.implicitly_wait(10)
        self.logger.info("adding wait for 10sec")

        self.lp = Listingpage(self.driver)
        self.logger.info("Initialized the Listing page object")

        self.lp.clickpopularfilter()
        self.logger.info("Click on Filter section ")

        self.lp.clicklowtohigh()
        self.logger.info("Click on Low to high filter")
        time.sleep(5)

        # self.driver.execute_script("window.scrollBy(0, 1000)")
        # time.sleep(10)

        self.lp.clicklogin()
        self.logger.info("Click on Login section")
        time.sleep(5)

        self.lp.clickcloselogin()
        self.logger.info("Click on close login section")
        time.sleep(3)

        self.lp.clickviewroom()
        self.logger.info("Click on view room section to move to next page.")
        time.sleep(3)
