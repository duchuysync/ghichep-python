from xvfbwrapper.xvfbwrapper import Xvfb
vdisplay = Xvfb(width=800, height=1280)
vdisplay.start()

import undetectedchromedriver.undetected_chromedriver.v2 as uc
import requests
from time import sleep

options = uc.ChromeOptions()
options.add_argument(f'--no-first-run --no-service-autorun --password-store=basic')
options.user_data_dir = f'./tmp/test_undetected_chromedriver'
options.add_argument(f'--disable-gpu')
options.add_argument(f'--no-sandbox')
options.add_argument(f'--disable-dev-shm-usage')

driver = uc.Chrome(
      options=options,
      headless=False)
with driver:
    driver.get('https://www.bambooairways.com/reservation/ibe/login')
    sleep(8)
    driver.find_element_by_css_selector("#login-agency-code").send_keys("0388719344")
    sleep(1)
    driver.find_element_by_css_selector("#login-agency-id").send_keys("0388719344")
    sleep(1)
    driver.find_element_by_css_selector("#login-password").send_keys("0388719344")
#        driver.save_screenshot("login.png");
    driver.find_element_by_css_selector("#loginForm > div.form > div:nth-child(7) > div > button").click()
    sleep(1)
#        driver.save_screenshot("pageImage.png");
    a = ("Bamboo;", driver.find_element_by_css_selector("#header > div.row > div > div > div.meta > div > div:nth-child(2) > div:nth-child(1) > strong").text)
    print(a)
#        driver    
##
##
vdisplay.stop()
