from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Classes_Google.google_start_page import InputField

o = Options()
o.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=o)
driver.get('https://www.google.ru/')
driver.find_element(By.XPATH, InputField.x_pass_way).click()
driver.find_element(By.XPATH, InputField.x_pass_way).send_keys('Курсы по PlayWright')
driver.find_element(By.XPATH, InputField.button_for_send).click()
html = driver.find_element(By.TAG_NAME, 'html')
for i in range (5):
    html.send_keys(Keys.DOWN)
driver.find_element(By.XPATH, InputField.hexlet_path).click()
driver.quit()
