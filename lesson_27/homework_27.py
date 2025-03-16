from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import selenium



# driver = webdriver.Safari()
#
# # Встановлення неявного очікування на 10 секунд
# driver.implicitly_wait(10)
#
#
# # Відкриття сайту ukr.net
# driver.get("https://www.ukr.net")
# # Приклад взаємодії: пошук елемента за тегом <body>
# try:
#     body_element = driver.find_element(By.TAG_NAME, "body")
#
#     print("Сторінка завантажена успішно.")
# except Exception as e:
#     print("Не вдалося знайти елемент на сторінці:", e)
#
# # Завершення роботи драйвера
# driver.quit()
#
#
# Ініціалізація драйвера
driver = webdriver.Safari()

# Встановлення неявного очікування на 10 секунд
driver.implicitly_wait(5)

# Відкриття сторінки входу ukr.net
driver.get("https://ukr.net/")  # Оновіть URL, якщо він інший

# Пошук полів вводу логіну та паролю
try:
    login_input = driver.find_element(By.CSS_SELECTOR, "#app-root > div > div > form > div:nth-child(1) > label > input")
    password_input = driver.find_element(By.CSS_SELECTOR, "#app-root > div > div > form > div:nth-child(2) > label > input")

    # Введення логіну та паролю
    login_input.send_keys("your_login")
    password_input.send_keys("your_password")

    # Імітація натискання Enter для входу
    password_input.send_keys(Keys.RETURN)

    print("Дані введено успішно!")

except Exception as e:
    print("Помилка при введенні даних:", e)

# Закриття браузера після виконання (зачекайте перед quit(), якщо треба перевірити результат)
driver.quit()
#
#
wait = WebDriverWait(driver, 5)

try:
    # Очікуємо, поки поле логіну стане доступним
    login_input = wait.until(EC.presence_of_element_located((By.NAME, "login")))
    password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))

    # Введення логіну та паролю
    login_input.send_keys("your_login")  # Замініть на свій логін
    password_input.send_keys("your_password")  # Замініть на свій пароль

    # Натискаємо Enter для входу
    password_input.send_keys(Keys.RETURN)

    # Очікуємо, поки сторінка після входу завантажиться (наприклад, кнопку "Вихід")
    wait.until(EC.presence_of_element_located((By.XPATH, '//a[contains(text(), "Вихід")]')))

    print("Вхід успішний!")

except Exception as e:
    print(f"Помилка: {e}")

finally:
    # Закриття браузера після виконання
    driver.quit()


# Запуск драйвера
driver = webdriver.Safari()
driver.get("https://ukr.net/")  # Оновіть URL, якщо він інший

# Ініціалізуємо явне очікування
wait = WebDriverWait(driver, 5)

# Очікуємо, поки текст "Пароль" з’явиться у потрібному елементі
wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "label"), "Пароль"))

print("Текст 'Пароль' став видимим!")

driver.quit()