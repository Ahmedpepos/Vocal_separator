from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import keyboard

def web_scrapper():
    service = Service(executable_path="D:\\Personal\\remove_music\\scrape\\chromedriver.exe")

    driver = webdriver.Chrome(service=service)

    driver.get("https://removevocals.ai/vocal-remover")

    # time.sleep(5)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "choose-btn"))
    )


    # driver.execute_script("arguments[0].style.display = 'block';","input[type='file']")
    # input_element = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
    input_element = driver.find_element(By.CLASS_NAME, "choose-btn")
    input_element.click()

    time.sleep(3)
    # input_element.send_keys("D:\Personal\remove_music\tennis.mp3")
    keyboard.write("D:\Personal\\remove_music\\tennis.mp3")
    keyboard.send("enter")



    # time.sleep(15)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Download Vocals')]"))
    )

    save_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Download Vocals')]")
    save_button.click()

    time.sleep(5)
#procView > div




if __name__ == "__main__" :
    web_scrapper()
