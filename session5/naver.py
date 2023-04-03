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


# 실행할 웹페이지 불러오기 (네이버 영화 페이지)
driver.get("https://movie.naver.com/")


# 랭킹 클릭해서 제목, 개요, 감독, 평점
btn = driver.find_element(By.XPATH, "/html/body/div/div[4]/div/div[1]/div[1]/button")
btn.click()
rankbtn = driver.find_element(By.XPATH, '//*[@id="scrollbar"]/div[1]/div/div/ul/li[3]/a')
rankbtn.click() 

file = open('naver.csv', mode='w', newline='')
writer = csv.writer(file)
writer.writerow(["title", "outline", "director", "rating"])

for i in range(2,23):
    rankbtn = driver.find_element(By.XPATH,f"/html/body/div/div[4]/div/div/div/div/div[1]/table/tbody/tr[{i}]/td[2]/div/a")
    rankbtn.click() 
    time.sleep(3)
    title = driver.find_element(By.XPATH,"/html/body/div/div[4]/div[2]/div[1]/div[2]/div[1]/h3/a[1]").text
    outline = driver.find_element(By.XPATH,"/html/body/div/div[4]/div[2]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[1]").text
    director = driver.find_element(By.XPATH,"/html/body/div/div[4]/div[2]/div[1]/div[2]/div[1]/dl/dd[2]/p/a").text
    rating = driver.find_element(By.XPATH,"/html/body/div/div[4]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/a/div/em").text
    print(title, outline, director, rating)
    time.sleep(3)
    moviebtn = driver.find_element(By.XPATH,'/html/body/div/div[3]/div/div[1]/div/div/ul/li[3]/a')
    moviebtn.click()
    writer.writerow([title, outline, director, rating]) 
file.close()

# # 좋아하는 영화, 제목, 감독, 평점, 리뷰 개수
# btn = driver.find_element(By.XPATH, "/html/body/div/div[4]/div/div[1]/div[1]/button")
# btn.click()
# qbtn = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/fieldset/div/span/input")
# qbtn.click()
# ActionChains(driver).send_keys('해리포터').perform()
# ActionChains(driver).send_keys(Keys.ENTER).perform()
# time.sleep(3)

# moviebtn = driver.find_element(By.XPATH,"/html/body/div/div[4]/div/div/div/div/div[1]/ul[2]/li[1]/dl/dt/a")
# moviebtn.click() 
# time.sleep(3)

# title = driver.find_element(By.XPATH,"/html/body/div/div[4]/div[3]/div[1]/div[2]/div[1]/h3/a").text
# director = driver.find_element(By.XPATH,"/html/body/div/div[4]/div[3]/div[1]/div[2]/div[1]/dl/dd[2]/p/a").text
# rating = driver.find_element(By.XPATH,"/html/body/div/div[4]/div[3]/div[1]/div[2]/div[1]/div[1]/div[3]/div[2]").text
# commens_num = driver.find_element(By.XPATH,"/html/body/div/div[4]/div[3]/div[1]/div[4]/div[5]/div[2]/div[3]/strong/em").text

# print(title, director, rating, commens_num)
# file = open('naver.csv', mode='w', newline='')
# writer = csv.writer(file)
# writer.writerow([title, director, rating, commens_num])
# file.close()




