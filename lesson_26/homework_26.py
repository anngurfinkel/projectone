
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time

# URL сайту
URL = "https://www.ukr.net"

driver = webdriver.Safari()
try:
    # Запускаємо Safari WebDriver
    driver.get(URL)

    # Очікуємо, поки сайт завантажиться
    wait = WebDriverWait(driver, 10)

    def scroll_page():
        """Функція для скролінгу сторінки"""
        print("📜 Скролимо сторінку вниз...")
        driver.execute_script("window.scrollBy(0, 1000);")  # Скрол на 1000px
        time.sleep(2)
        print("✅ Скролінг виконано!")

    def hover_over_links():
        """Функція для наведення мишки на посилання без кліку"""
        print("🖱️ Водимо мишкою над посиланнями...")

        # Знаходимо всі посилання на сторінці
        links = driver.find_elements(By.TAG_NAME, "a")
        action = ActionChains(driver)

        hovered_count = 0  # Лічильник наведених посилань

        for link in links:
            href = link.get_attribute("href")
            if href and link.is_displayed():
                print(f"🎯 Наводимо мишку на: {href}")

                # Прокручуємо до елемента перед наведенням
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", link)
                time.sleep(1)  # Чекаємо, щоб браузер оновив вигляд

                try:
                    action.move_to_element(link).perform()  # Наводимо мишку на посилання
                    hovered_count += 1
                    time.sleep(1)  # Невелика пауза між наведеннями
                except Exception as e:
                    print(f"❌ Не вдалося навести мишку: {e}")

                if hovered_count >= 5:  # Наводимо мишку тільки на перші 5 посилань
                    break

        print("✅ Наведення мишкою завершено!")

    # Виконуємо скролінг
    scroll_page()

    # Водимо мишкою над посиланнями
    hover_over_links()

    # Робимо скріншот після наведених посилань
    screenshot_path = "ukrnet_after_hover.png"
    driver.save_screenshot(screenshot_path)
    print(f"📸 Скріншот збережено: {screenshot_path}")

except Exception as e:
    print(f"❌ Виникла помилка: {e}")

finally:
    # Закриваємо браузер у будь-якому випадку
    driver.quit()
    print("🚀 Тест завершено!")
