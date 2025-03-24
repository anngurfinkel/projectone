import pytest
from selenium import webdriver
from page_objects.registration_page import RegistrationPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_registration(driver):
    # Створюємо екземпляр сторінки реєстрації
    registration_page = RegistrationPage(driver)
    
    # Перехід на сторінку реєстрації
    driver.get("https://platform.labelyourdata.com/sign-up")
    
    # Натискання на кнопку "Sign up using email"
    registration_page.get_sign_up_button().click()
    
    # Заповнення полів для реєстрації
    registration_page.enter_username("test_user")
    registration_page.enter_email("test_user@example.com")
    registration_page.enter_password("TestPassword123!")
    registration_page.enter_confirm_password("TestPassword123!")
    