from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys('a')
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys('a')
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys('a')
    input_file = browser.find_element(By.CSS_SELECTOR, "input[type='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, '1.txt')           # добавляем к этому пути имя файла 
    input_file .send_keys(file_path)
    time.sleep(1)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()