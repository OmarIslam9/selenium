import time

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_drive="/Users/Islam/OneDrive/Desktop/chromedriver.exe"
driver=webdriver.Chrome(executable_path=chrome_drive)
driver.get("https://www.linkedin.com/home?original_referer=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2F")
time.sleep(5)
user=driver.find_element(By.XPATH,'//*[@id="session_key"]')
user.send_keys("omarislam2546@gmail.com")
time.sleep(5)
password=driver.find_element(By.XPATH,'//*[@id="session_password"]')
password.send_keys("3omarIslam@l")
time.sleep(5)
sign=driver.find_element(By.XPATH,'//*[@id="main-content"]/section[1]/div/div/form/button')
sign.click()
time.sleep(10)


po=driver.find_element(By.XPATH,'//*[@id="ember293"]/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[1]')
po.send_keys("this is the first automated post i made by selenium")
time.sleep(5)
b=driver.find_element(By.XPATH,'//*[@id="ember317"]/span')
b.click()
time.sleep(10)
