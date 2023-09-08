from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://instagram.com')
time.sleep(3)

email = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')
email.send_keys('neolich86@gmail.com')
pw = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
pw.send_keys('@2dlckdgus')

enter = driver.find_element(By.CSS_SELECTOR, '._acap')
enter.send_keys(Keys.ENTER)
time.sleep(5)

driver.get('https://www.instagram.com/yooonmarch/')
time.sleep(5)
first = driver.find_element(By.CSS_SELECTOR, '._aagw')
driver.execute_script('arguments[0].click();', first)
time.sleep(3)

for i in range(10):
    try:
        like = driver.find_element(By.CSS_SELECTOR, 'body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe.x1qjc9v5.xjbqb8w.x1lcm9me.x1yr5g0i.xrt01vj.x10y3i5r.xr1yuqi.xkrivgy.x4ii5y1.x1gryazu.x15h9jz8.x47corl.xh8yej3.xir0mxb.x1juhsu6 > div > article > div > div._ae65 > div > div > div._ae2s._ae3v._ae3w > section._aamu._ae3_._ae47._ae48 > span._aamw > div')
        driver.execute_script('arguments[0].click();', like)
        time.sleep(3)
        # 다음 버튼 클릭하기
        driver.find_element(By.CSS_SELECTOR, '._aaqg ._abl-').click()
        time.sleep(3)
    except:
        # 다음 버튼 클릭하기
        driver.find_element(By.CSS_SELECTOR, '._aaqg ._abl-').click()
