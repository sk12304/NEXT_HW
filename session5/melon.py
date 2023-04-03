from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import csv
from selenium.webdriver.common.action_chains import ActionChains


# 디버깅 모드
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_driver = 'C:/Users/sk041/Desktop/NEXT_HW/Session5/chromedriver.exe'
driver = webdriver.Chrome(chrome_driver, options= chrome_options)

# 실행할 웹페이지 불러오기 (멜론 차트)
driver.get("https://www.melon.com/index.htm")

# 멜론 차트 버튼 클릭
# chartbtn = driver.find_element(By.XPATH, '//*[@id="gnb_menu"]/ul[1]/li[1]/a/span[2]')
# chartbtn.click()


# # 1위곡명 가져오기
# first = driver.find_element(By.XPATH, '//*[@id="lst50"]/td[6]/div/div/div[1]/span/a').text
# time.sleep(3)
# print(first)

# 1위부터 20위까지 가져오기
# for i in range(1,21):
#     titles = driver.find_element(By.XPATH,f"/html/body/div/div[3]/div/div/div[3]/form/div/table/tbody/tr[{i}]/td[6]/div/div/div[1]/span/a").text
#     time.sleep(3)
#     print(titles)

# 스크롤 내리기

# 실시간 급상승 가수 가져오기
# first = driver.find_element(By.XPATH, '//*[@id="gnb"]/div[2]/div/ol')
# ActionChains(driver).move_to_element(first).perform()
# for i in range(1,11):
#     second = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div[2]/div/ol/li[{i}]/a').text
#     time.sleep(3)
#     print(second)
# 정답은 사진 확인, 이건 틀림


# 곡의 장르 가져오기
# chartbtn = driver.find_element(By.XPATH, '///*[@id="lst50"]/td[7]/div/div/div/a')
# chartbtn.click()
# time.sleep(3)
# first = driver.find_element(By.XPATH, '//*[@id="conts"]/div[2]/div/div[2]/div[2]/dl/dd[2]').text
# time.sleep(3)
# print(first)


# 좋아하는 가수의 곡명 10개
# chartbtn = driver.find_element(By.XPATH, '//*[@id="top_search"]')
# chartbtn.click()
# ActionChains(driver).send_keys('아이유').perform()
# qbtn = driver.find_element(By.XPATH, '//*[@id="gnb"]/fieldset/button[2]/span')
# qbtn.click()
# for i in range(1,11):
#     titles = driver.find_element(By.XPATH,f"/html/body/div/div[3]/div/div[1]/div[4]/div/form[1]/div/table/tbody/tr[{i}]/td[3]/div/div/a[2]").text
#     time.sleep(3)
#     print(titles)


# 순위, 곡명, 가수명 가져오기
chartbtn = driver.find_element(By.XPATH, '//*[@id="gnb_menu"]/ul[1]/li[1]/a/span[2]')
chartbtn.click()

file = open('melon.csv', mode"w", newline='')
writer = csv.writer(file)
writer.writerow(["i", "titles","name"])

for i in range(1,51):
    titles = driver.find_element(By.XPATH,f"/html/body/div/div[3]/div/div/div[3]/form/div/table/tbody/tr[{i}]/td[6]/div/div/div[1]/span/a").text
    name = driver.find_element(By.XPATH,f"/html/body/div/div[3]/div/div/div[3]/form/div/table/tbody/tr[{i}]/td[6]/div/div/div[2]/a").text 
    print(i, titles, name)
    writer.writerow([i, titles, name])
file.close()


# csv 파일로 변환

