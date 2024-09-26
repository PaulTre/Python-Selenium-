from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




driver = webdriver.Chrome()

class InputField:
    x_pass_way = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea'
    button_for_send = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[4]/div[6]/center/input[1]'
    hexlet_path = '/html/body/div[3]/div/div[13]/div/div[2]/div[2]/div/div/div[7]/div/div/div[1]/div/div/span/a/h3'


    @staticmethod
    def press_input(xpath):
        wait = WebDriverWait(driver, 20)  # Установка времени ожидания
        return wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))  # Обратите внимание на кортеж


