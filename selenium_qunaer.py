from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

chrome_driver = 'E:\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver)
for i in ['https://www.baidu.com/','https://www.baidu.com/','https://www.baidu.com/']:
    driver.get(i)



