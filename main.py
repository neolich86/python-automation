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

"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://etk.srail.co.kr/cmc/01/selectLoginForm.do')
time.sleep(1)

# 로그인
driver.find_element(By.ID, 'srchDvNm01').send_keys('1791063009') # 회원번호
driver.find_element(By.ID, 'hmpgPwdCphd01').send_keys("@2dlckdgus") # 비밀번호
driver.find_element(By.XPATH, '//*[@id="login-form"]/fieldset/div[1]/div[1]/div[2]/div/div[2]/input').click()
time.sleep(2)

# 기차 조회 페이지로 이동
driver.get('https://etk.srail.kr/hpg/hra/01/selectScheduleList.do')
time.sleep(2)

# 출발지 입력
dep_stn = driver.find_element(By.ID, 'dptRsStnCdNm')
dep_stn.clear()
dep_stn.send_keys("수서")

# 도착지 입력
arr_stn = driver.find_element(By.ID, 'arvRsStnCdNm')
arr_stn.clear()
arr_stn.send_keys("부산")
time.sleep(1)

# 출발 날짜
elm_dptDt = driver.find_element(By.ID, "dptDt")
driver.execute_script("arguments[0].setAttribute('style','display: True;')", elm_dptDt)
Select(driver.find_element(By.ID,"dptDt")).select_by_index(1)

# 출발 시간
elm_dptTm = driver.find_element(By.ID, "dptTm")
driver.execute_script("arguments[0].setAttribute('style','display: True;')", elm_dptTm)
Select(driver.find_element(By.ID, "dptTm")).select_by_visible_text("20")

# 조회하기 버튼 클릭
driver.find_element(By.XPATH, "//input[@value='조회하기']").click()
time.sleep(1)

reserved = False

while True:
    for i in range(1, 5):
        standard_seat = driver.find_element(By.CSS_SELECTOR, f"#result-form > fieldset > div.tbl_wrap.th_thead > table > tbody > tr:nth-child({i}) > td:nth-child(7)").text

        if "예약하기" in standard_seat:
            print("예약 가능")
            driver.find_element(By.XPATH, f"/html/body/div[1]/div[4]/div/div[3]/div[1]/form/fieldset/div[6]/table/tbody/tr[{i}]/td[7]/a/span").click()
            time.sleep(10)
            reserved = True
            driver.find_element(By.XPATH, "//*[@id='list-form']/fieldset/div[11]/a[1]/span").click()
            time.sleep(1)
            driver.find_element(By.XPATH, "//*[@id='chTab2']").click()
            time.sleep(1)
            driver.find_element(By.XPATH, "//*[@id='agreeTmp']").click()
            time.sleep(1)
            driver.find_element(By.XPATH, "//*[@id='requestIssue2']").click()
            time.sleep(1)
            break

    if not reserved:
        # 5초 기다리기
        time.sleep(5)

        # 다시 조회하기
        submit = driver.find_element(By.XPATH, "//input[@value='조회하기']")
        driver.execute_script("arguments[0].click();", submit)
        print("새로고침")
        time.sleep(1)
    else:
        break
"""