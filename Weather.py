from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time

options = Options()
#options.add_argument("headless")
driver_path = '/Users/kalekamara/Downloads/chromedriver 2'

driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://weather.com/weather/today/l/a09893d779e36b000fe919e71aaf41c57190c5a9f2844fe295b041b99148853a')

city = driver.find_element(By.XPATH,'//*[@id="WxuHeaderLargeScreen-header-9944ec87-e4d4-4f18-b23e-ce4a3fd8a3ba"]/header/div/div[2]/div[1]/div/div[1]/svg')
city.click()
city.send_keys('duluth')

weather = driver.find_element(By.XPATH,'//*[@id="WxuCurrentConditions-main-eb4b02cb-917b-45ec-97ec-d4eb947f6b6a"]/div/section/div/div[2]/div[1]/div[1]/span')

#
# temp = weather.text
# temp2= int(temp.strip('°'))
# cel = (temp2-32)*5/9
# print(cel)
#
# # time.sleep(5)
# # driver.quit()