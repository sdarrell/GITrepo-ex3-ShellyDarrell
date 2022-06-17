from selenium import webdriver

from os.path import basename

# path to the chosen web driver
xpath = "C://Users//Shelly//Documents//chromedriver.exe"


def place_orders(rest, day, driver, loop=True, flag=0):
    order_element = '//*[@id="mainTBL"]/tbody/tr[{}]/td[{}]/img'.format(rest, day)
    while loop:

        loop = False

        # try starting placing orders
        try:

            # start running on days elements
            element = driver.find_element_by_xpath(order_element)
            element.click()
            driver.implicitly_wait(30)

            # search for a clean order tab
            element = driver.find_element_by_xpath('//*[@id="Continue"]')
            if element.is_displayed():
                flag = 1
            else:
                # if this day already ordered - close popup and move to the next day
                element = driver.find_element_by_xpath('//*[@id="fancybox-close"]')
                element.click()
                driver.implicitly_wait(30)
                return flag

            # proceed with the order
            element = driver.find_elements_by_xpath("//input[@name='name' and @value='המשך']")[0]
            element.click()
            driver.implicitly_wait(30)

            # choose last favorite meal
            element = driver.find_element_by_xpath('//*[@id="selectDishFromLastOrderLink"]')
            element.click()
            driver.implicitly_wait(30)

            # approve
            element = driver.find_element_by_xpath('//*[@id="addItemToCartTopTd"]/input')
            element.click()
            driver.implicitly_wait(30)
        except:
            pass

        # searching for popup errors
        try:
            # search for frozen box error
            element = driver.find_element_by_xpath('//*[@id="fancybox-inner"]')
            if element.is_displayed():
                try:
                    element = driver.find_element_by_xpath('//*[@id="fancybox-close"]')
                    element.click()
                    driver.implicitly_wait(30)
                    driver.refresh()
                    driver.implicitly_wait(30)
                    loop = True
                    flag = 0
                except:
                    pass
        except:
            pass

    return flag


def configure_elements():
    chrome_options = webdriver.ChromeOptions()

    # disable web slowness by removing extensions and proxies
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument('--no-proxy-server')
    chrome_options.add_argument("--headless")

    # Optional argument, if not specified will search path
    driver = webdriver.Chrome(xpath, options=chrome_options)

    # load working web page
    # check fits page can be opened
    print('testing first page with selenium')
    driver.get('http://localhost:8090/ShellyD/Register_1.jsp')
    driver.implicitly_wait(30)
    print('first test was succeeded')
    
    # check second page is working
    print('testing second page with selenium')
    element = driver.find_element_by_xpath('/html/body/form/input')
    element.click()
    driver.implicitly_wait(30)
    print('second test was succeeded')


def main():
    configure_elements()


if __name__ == '__main__':
    main()
