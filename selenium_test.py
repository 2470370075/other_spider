from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import xlwt

option = Options()
option.add_argument('--headless')

chrome_driver = 'E:\chromedriver.exe'
driver = webdriver.Chrome(chrome_options=option,executable_path=chrome_driver)

driver.get('https://www.jd.com/?cu=true&utm_source=baidu-pinzhuan&utm_medium=cpc&utm_campaign=t_288551095_baidupinzhuan&utm_term=0f3d30c8dba7459bb52f2eb5eba8ac7d_0_0097a72d863b49999dfb8264d866c91c')

kw = driver.find_element_by_id('key')
print(kw.get_attribute('class'))
kw.send_keys('pythonjava')

kw.send_keys(Keys.RETURN)

time.sleep(1)

sele = driver.find_element_by_xpath('//div[@class="f-sort"]/a[2]')
sele.click()
workbook = xlwt.Workbook(encoding='utf-8')
sheet = workbook.add_sheet('sheet1',cell_overwrite_ok=True)
c = 0
while 1:

    time.sleep(1)
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(1)

    book = driver.find_elements_by_xpath('//li[@class="gl-item"]')

    time.sleep(1)

    for i in book:

        dic = {}
        name = i.find_element_by_xpath('.//div[@class="p-name"]//em').text
        price = i.find_element_by_xpath('.//div[@class="p-price"]//i').text
        dic[name] = price

        print(dic)

        sheet.write(c,0,name)
        sheet.write(c,1,price)
        workbook.save('book.xls')
        c += 1

    try:
        next_page = driver.find_element_by_xpath('//div[@id="J_bottomPage"]//a[@class="pn-next"]')
        next_page.click()
    except:
        break

driver.quit()



