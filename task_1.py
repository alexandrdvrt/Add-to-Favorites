from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
from selenium.webdriver.common.keys import Keys

# Инициализация WebDriver для Chrome
driver = webdriver.Chrome()

# Переход на страницу избранных объявлений
driver.get("https://www.avito.ru/favorites")

try:
    # Попытка добавления объявлений в избранное
    ads_to_add = ["https://www.avito.ru/murmansk/knigi_i_zhurnaly/knigi_konstruirovanie_odezhdy_3316253424", "https://www.avito.ru/novorossiysk/kvartiry/prodam-ASgBAgICAUSSA8YQ","https://www.avito.ru/novorossiysk/gotoviy_biznes/zavod_po_proizvodstvu_gazobetona_rtm-60ka_3274229497"]  # Замените на реальные URL объявлений

    for ad_url in ads_to_add:
        driver.get(ad_url)
        time.sleep(random.uniform(5, 10))
        try:
            add_to_favorites_button = driver.find_element(By.XPATH, "//button[@title='Добавить в избранное' and @class='desktop-usq1f1']")
            add_to_favorites_button.click()
            time.sleep(random.uniform(5, 10))
        except:
            add_to_favorites_button = driver.find_element(By.XPATH, "//div[@title='Добавить в избранное и в сравнение']")
            add_to_favorites_button.click()
            time.sleep(random.uniform(5, 10))

    # Проверка, что добавленные объявления отображаются на странице избранных
    driver.get("https://www.avito.ru/favorites")
    time.sleep(random.uniform(1, 3))
    xpath_expression = "//div[@class='item-snippet-root-d2wFO']"
    favorite_ads = driver.find_elements(By.XPATH, xpath_expression)
    count = len(favorite_ads)
    time.sleep(random.uniform(5, 10))

    assert len(favorite_ads) == len(ads_to_add), "Количество добавленных объявлений не соответствует ожидаемому"

    # Попытка удаления объявлений из избранного
    for ad_title in favorite_ads:
        #ad_title.click()
        driver.get("https://www.avito.ru/favorites")
        remove_from_favorites_button = driver.find_element(By.XPATH, "//div[@class='withFavorites-heart-x57Yw withFavorites-heart_fill-InZcS']")
        remove_from_favorites_button.click()
        time.sleep(random.uniform(5, 10))

    # Проверка, что объявления успешно удалены из списка избранных
    driver.get("https://www.avito.ru/favorites")
    xpath_expression = "//div[@class='item-snippet-root-d2wFO']"
    favorite_ads_after_removal = driver.find_elements(By.XPATH, xpath_expression)

    time.sleep(random.uniform(1, 3))

    assert len(favorite_ads_after_removal) == 0, "Объявления не были удалены из избранного"

except Exception as e:
    print(f"Тест завершился с ошибкой: {str(e)}")
else:
    print("good")
finally:
    # Закрытие браузера после выполнения теста
    driver.quit()
