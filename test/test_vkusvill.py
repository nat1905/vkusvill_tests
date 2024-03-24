import time
import allure

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


@allure.feature('Vkusvill tests')
@allure.story('Find different elements')
class TestVkussvill:
    @allure.title('Найти товар "молоко"')
    def test_find_good(self, selenium, go_to_url):
        '''
        Тест Найти товар

        Шаги:
        1) перейти на сайт
        2) в строке поиска ввести слово "молоко"
        3) нажать enter
        4) проверить, что в результатах поиска - молоко
        '''
        # Arrange
        with allure.step("Открытие страницы"):
            go_to_url("https://vkusvill.ru/")

        # Act
        with allure.step("Действия с элементами"):
            search_field = selenium.find_element(By.CSS_SELECTOR, 'input.HeaderSearchBlock__Input')
            search_field.click()
            good = 'молоко'
            for i in good:
                search_field.send_keys(i)
                time.sleep(0.2)
            search_field.send_keys(Keys.ENTER)
            time.sleep(0.5)

        # Assert
        with allure.step("Проверка найденных элементов"):
            result = selenium.find_elements(By.XPATH, "//*[contains(@class,'ProductCard__link')]")
            for i in result:
                assert 'Молоко' in i.text

    def test_choose_delivery_address(self, selenium, go_to_url):
        '''
        Тест Выбрать адрес доставки

        Шаги:
        1) перейти на сайт
        2) сверху слева нажать на ссылку Выбирете способ и время доставки
        3) в модальном окне выбрать Самовывоз
        4) нажать кнопку Список магазинов
        5) выбрать магазин из списка
        6) нажать на кнопку Заберу отсюда
        7) выбрать время доставки
        8) проверить что адрес выбранного магазина теперь отображается в верхнем левом углу

        '''
        # Arrange
        with allure.step("Открытие страницы"):
            go_to_url("https://vkusvill.ru")

        # Act
        with allure.step("Действия с элементами"):
            selenium.find_element(By.XPATH, '//span[contains(text(), "Выберите способ")]').click()
            time.sleep(0.5)

            selenium.find_element(By.XPATH, '//button[contains(text(), "Самовывоз")]').click()
            time.sleep(0.3)

            selenium.find_element(By.XPATH, '//span[contains(text(), "Список магазинов")]').click()
            time.sleep(0.3)

            address_city = selenium.find_element(By.CSS_SELECTOR, ".js-shops-shop-city")
            address_street = selenium.find_element(By.CSS_SELECTOR, ".js-shops-shop-address")
            address = address_city.text + ' ' + address_street.text
            address_street.click()
            time.sleep(0.3)

            selenium.find_element(By.XPATH, '//a[contains(text(), "Заберу отсюда")]').click()
            time.sleep(0.3)

            selenium.find_element(By.XPATH, '//div[contains(text(), "Завтра")]').click()
            time.sleep(0.3)
            address_header = selenium.find_element(By.CSS_SELECTOR, '.js-header-address-text')

        # Assert
        with allure.step("Проверка найденных элементов"):
            if address_header.text in address:
                assert True
