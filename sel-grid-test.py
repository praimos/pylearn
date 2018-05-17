from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver

selenium_grid_url = 'http://25.20.66.191:4444/wd/hub'
capabilities = DesiredCapabilities.CHROME

driver = webdriver.Remote(command_executor=selenium_grid_url,
                          desired_capabilities=capabilities)
# driver2 = webdriver.Chrome('C:\\Users\\aneshumov\\'
#                            'Documents\\selenium\\chromedriver.exe')

driver.get("http://google.com")
print(driver.title)

driver.close()
