from selenium import webdriver
import time 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import options
import io
import sys
from selenium.common.exceptions import NoSuchElementException
import pyautogui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random


chrome_options = Options()
options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("user-data-dir=C:\\Users\\gabri\\Local\Google\\Chrome\\")
# make sure the path is already logged into your ok cupid account
options.add_argument('--profile-directory=Profile 1') #Path to your chrome profile

driver = webdriver.Chrome(options=options, executable_path=r'C:\Program Files (x86)\Chrome\Application\chromedriver.exe')
driver.get('https://okcupid.com')
# let page load
time.sleep(10)

def main():
    try:
        driver.find_element_by_class_name('messenger-user-row-close').click()
    except NoSuchElementException:
        like = driver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[3]/div/div[1]/div/div/div/div/div[1]/div[2]/button[2]').click()
        dislike = driver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[3]/div/div[1]/div/div/div/div/div[1]/div[2]/button[1]').click()
        choose = random.choice([like, dislike])
        print('success')
        time.sleep(4)
        try:
            driver.find_element_by_class_name('connection-view-container-close-button').click()
            print('New Match.')
        except NoSuchElementException:
            main()


while True:
    main()
