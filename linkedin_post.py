from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

USERNAME = 'your_email@example.com'
PASSWORD = 'your_password'
POST_TEXT = '🚀 This is an automated LinkedIn post using Python! #python #automation'

driver = webdriver.Chrome()

try:
   
    driver.get("https://www.linkedin.com/login")
    time.sleep(2)

    driver.find_element(By.ID, "username").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "password").send_keys(Keys.RETURN)
    time.sleep(3)


    driver.get("https://www.linkedin.com/feed/")
    time.sleep(5)
    driver.find_element(By.CLASS_NAME, "share-box-feed-entry__trigger").click()
    time.sleep(3)

    post_input = driver.find_element(By.CLASS_NAME, "ql-editor")
    post_input.click()
    post_input.send_keys(POST_TEXT)
    time.sleep(1)

    post_buttons = driver.find_elements(By.XPATH, "//button[contains(@aria-label, 'Post')]")
    for btn in post_buttons:
        if btn.is_displayed():
            btn.click()
            break

    print(" Successfully posted on LinkedIn.")
    time.sleep(5)

finally:
    driver.quit()
