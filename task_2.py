from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time

# Измените на URL объявления, на которое вы хотите провести тест
AD_URL = "https://www.avito.ru/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363"

driver = webdriver.Chrome()

# Открытие страницы объявления
driver.get(AD_URL)

try:
    # Нахождение и нажатие на кнопку "Добавить в избранное"
    favorite_button = driver.find_element(By.XPATH, "//button[@title='Добавить в избранное' and @class='desktop-usq1f1']")
    favorite_button.click()
    time.sleep(3)
    # Подтверждение, что объявление добавлено в избранное
    confirmation_message = driver.find_element(By.XPATH, "//span[contains(text(),'В избранном')]").text
    assert "в избранном" in confirmation_message.lower()

except Exception as e:
    print(f"Тест провален: {e}")
else:
    print("Тест успешно выполнен")

finally:
    # Закрытие браузера после выполнения теста
    driver.quit()
