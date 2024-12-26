from selene import browser
import pytest


@pytest.fixture(scope='session', autouse=True)
def browser_start():
    browser.config.base_url = 'https://github.com'

    yield

    print("\nТестирование завершено. Закрываем браузер!")
    browser.quit()
